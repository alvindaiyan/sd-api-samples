import base64
import copy
import json
import time
from datetime import datetime
from io import BytesIO
from txt2img_param import txt2img_param
from img2img_param import img2img_param

import requests
from PIL import Image, PngImagePlugin


class PythonAPISamples:

    def __init__(self, api_url: str, api_token: str, user_id: str):
        self.api_url = api_url
        self.api_token = api_token
        self.user_id = user_id

    def txt2img(self, models: dict, param: str) -> str:
        inference_id = self._create_inference_job(models=models, inference_param=param, is_img2img=False)
        self._get_inference_result(inference_id, False)
        return inference_id

    def img2img(self, models: dict, param: str):
        inference_id = self._create_inference_job(models=models, inference_param=param, is_img2img=True)
        self._get_inference_result(inference_id, True)
        return inference_id

    def _get_inference_result(self, inference_id: str, is_img2img: bool):
        time.sleep(3)
        inference_job_resp = self._get_inference_job(inference_id)
        while inference_job_resp and inference_job_resp['status'] == "inprogress":
            time.sleep(3)
            inference_job_resp = self._get_inference_job(inference_id)

        images = self._get_inference_job_image_output(inference_id.strip())
        inference_param_json_list = self._get_inference_job_param_output(inference_id)
        output_folder = 'txt2img' if not is_img2img else 'img2img'
        if inference_job_resp['status'] == "succeed":
            image_list = self._download_images_to_pil(images)
            json_file = self._download_images_to_json(inference_param_json_list)[0]
            for (i, img) in enumerate(image_list):
                img.save(f'output/{output_folder}/result_{inference_id}_{i}.png')

            with open(f'output/{output_folder}/metadata_{inference_id}.json', 'w') as f:
                f.write(json_file)

    def _get_inference_job(self, inference_job_id):
        response = requests.get(f'{self.api_url}inference/get-inference-job?jobID={inference_job_id}', headers = {
            "x-api-key": self.api_token,
            "Content-Type": "application/json"
        })
        return response.json()

    def _get_inference_job_image_output(self, inference_job_id):
        try:
            response = requests.get(f'{self.api_url}inference/get-inference-job-image-output?jobID={inference_job_id}',
                                    headers={
                                        "x-api-key": self.api_token,
                                        "Content-Type": "application/json"
                                    })
            r = response.json()
            txt2img_inference_job_image_list = []
            for obj in r:
                obj_value = str(obj)
                txt2img_inference_job_image_list.append(obj_value)
            return txt2img_inference_job_image_list
        except Exception as e:
            print(f"An error occurred while getting inference job image output: {e}")
            return []

    def _download_images_to_pil(self, image_urls: list):
        image_list = []
        for url in image_urls:
            try:
                response = requests.get(url)
                response.raise_for_status()
                from PIL import Image
                import io
                pil_image = Image.open(io.BytesIO(response.content))
                image_list.append(pil_image)
            except requests.exceptions.RequestException as e:
                print(f"Error downloading image {url}: {e}")
        return image_list

    def _download_images_to_json(self, image_urls: list):
        results = []
        for url in image_urls:
            try:
                response = requests.get(url)
                response.raise_for_status()
                json_resp = response.json()
                results.append(json_resp['info'])
            except requests.exceptions.RequestException as e:
                print(f"Error downloading image {url}: {e}")
        return results

    def _get_inference_job_param_output(self, inference_job_id):
        try:
            response = requests.get(f'{self.api_url}inference/get-inference-job-param-output?jobID={inference_job_id}',
                                    headers={
                                        "x-api-key": self.api_token,
                                        "Content-Type": "application/json"
                                    })
            r = response.json()
            txt2img_inference_job_param_list = []
            for obj in r:
                obj_value = str(obj)
                txt2img_inference_job_param_list.append(obj_value)
            return txt2img_inference_job_param_list
        except Exception as e:
            print(f"An error occurred while getting inference job param output: {e}")
            return []

    def _create_inference_job(self, models, inference_param, is_img2img) -> str:
        payload = {
            'user_id': self.user_id,
            'task_type': "txt2img" if not is_img2img else 'img2img',
            'models': models,
            'filters': {
                'createAt': datetime.now().timestamp(),
                'creator': 'sd-webui'
            }
        }

        inference_id = None

        # first, we create an inference job
        response = requests.post(f'{self.api_url}inference/v2', json=payload, headers={'x-api-key': self.api_token})
        response.raise_for_status()
        upload_param_response = response.json()
        if upload_param_response['statusCode'] != 200:
            raise Exception(upload_param_response['errMsg'])

        if 'inference' in upload_param_response and \
                'api_params_s3_upload_url' in upload_param_response['inference']:
            # second, we upload the inference parameter to s3
            upload_s3_resp = requests.put(upload_param_response['inference']['api_params_s3_upload_url'], data=inference_param)
            upload_s3_resp.raise_for_status()

            inference_id = upload_param_response['inference']['id']

            # last, start run infer
            response = requests.put(f'{self.api_url}inference/v2/{inference_id}/run', json=payload,
                                    headers={'x-api-key': self.api_token})
            response.raise_for_status()

        return inference_id

    def _get_header(self):
        pass

    def decode_base64_to_image(self, encoding: str) -> Image.Image:
        image_encoded = self.extract_base64_data(encoding)
        img = Image.open(BytesIO(base64.b64decode(image_encoded)))
        return img

    def extract_base64_data(self, x: str) -> str:
        """Just extracts the base64 data from a general base64 string."""
        return x.rsplit(",", 1)[-1]

    def encode_image_to_base64(self, image_path) -> str:
        img = Image.open(image_path)
        return self.encode_pil_to_base64(img)

    def encode_pil_to_base64(self, pil_image):
        with BytesIO() as output_bytes:
            pil_image.save(output_bytes, "PNG", pnginfo=self.get_pil_metadata(pil_image))
            bytes_data = output_bytes.getvalue()

        base64_str = str(base64.b64encode(bytes_data), "utf-8")
        return "data:image/png;base64," + base64_str

    def get_pil_metadata(self, pil_image):
        # Copy any text-only metadata
        metadata = PngImagePlugin.PngInfo()
        for key, value in pil_image.info.items():
            if isinstance(key, str) and isinstance(value, str):
                metadata.add_text(key, value)

        return metadata


if __name__ == '__main__':
    sample_client = PythonAPISamples(
        api_url='https://{api-gateway}.execute-api.{region}.amazonaws.com/prod/',
        api_token='token',
        user_id='flash'
    )

    # txt2img example:
    controlnet_img_path = 'controlnet_img_sample.jpg'
    controlnet_img_mask_path = 'mask.png'
    txt2img_param = copy.deepcopy(txt2img_param)

    txt2img_param['alwayson_scripts']['controlnet']['args'][0]['module'] = 'canny'
    txt2img_param['alwayson_scripts']['controlnet']['args'][0]['enabled'] = True
    txt2img_param['alwayson_scripts']['controlnet']['args'][0]['image']['image'] = sample_client.encode_image_to_base64(controlnet_img_path)
    txt2img_param['alwayson_scripts']['controlnet']['args'][0]['image']['mask'] = sample_client.encode_image_to_base64(controlnet_img_mask_path)

    infer_id = sample_client.txt2img(
        models={
            'Stable-diffusion': ['kakarot11825DCozy.G2sZ.safetensors'],
            'ControlNet': ['control_v11p_sd15_canny.pth'],
            'VAE': ['vae-ft-mse-840000-ema-pruned.safetensors'],
            'embeddings': ['badhandv4.SR0q.pt', 'badPromptVersion2.H5lf.pt', 'bad-hands-5.pt', 'EasyNegative.safetensors']
        },
        param=json.dumps(txt2img_param)
    )

    # img2img example:
    img2img_param = copy.deepcopy(img2img_param)
    img2img_param['alwayson_scripts']['controlnet']['args'][0]['module'] = 'canny'
    img2img_param['alwayson_scripts']['controlnet']['args'][0]['enabled'] = True
    img2img_param['init_images'] = [sample_client.encode_image_to_base64(controlnet_img_path)]

    sample_client.img2img(
        models={
            'Stable-diffusion': ['kakarot11825DCozy.G2sZ.safetensors'],
            'ControlNet': ['control_v11p_sd15_canny.pth'],
            'VAE': ['vae-ft-mse-840000-ema-pruned.safetensors'],
            'embeddings': ['badhandv4.SR0q.pt', 'badPromptVersion2.H5lf.pt', 'bad-hands-5.pt', 'EasyNegative.safetensors']
        },
        param=json.dumps(img2img_param)
    )
