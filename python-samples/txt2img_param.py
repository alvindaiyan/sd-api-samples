txt2img_param = {
    "prompt": "man, warrior, handsome, bald",
    "negative_prompt": "old, bad quality",
    "styles": [],
    "seed": -1,
    "subseed": -1,
    "subseed_strength": 0.0,
    "seed_resize_from_h": -1,
    "seed_resize_from_w": -1,
    "sampler_name": "DPM++ 2M Karras",
    "batch_size": 1,
    "n_iter": 1,
    "steps": 20,
    "cfg_scale": 7.0,
    "width": 512,
    "height": 512,
    "restore_faces": None,
    "tiling": None,
    "do_not_save_samples": False,
    "do_not_save_grid": False,
    "eta": None,
    "denoising_strength": None,
    "s_min_uncond": 0.0,
    "s_churn": 0.0,
    "s_tmax": float('inf'),
    "s_tmin": 0.0,
    "s_noise": 1.0,
    "override_settings": {},
    "override_settings_restore_afterwards": True,
    "refiner_checkpoint": None,
    "refiner_switch_at": None,
    "disable_extra_networks": False,
    "comments": {},
    "enable_hr": False,
    "firstphase_width": 0,
    "firstphase_height": 0,
    "hr_scale": 2.0,
    "hr_upscaler": "Latent",
    "hr_second_pass_steps": 0,
    "hr_resize_x": 0,
    "hr_resize_y": 0,
    "hr_checkpoint_name": None,
    "hr_sampler_name": None,
    "hr_prompt": "",
    "hr_negative_prompt": "",
    "sampler_index": "DPM++ 2M Karras",
    "script_name": None,
    "script_args": [],
    "send_images": True,
    "save_images": False,
    "alwayson_scripts": {
        "refiner": {
            "args": [
                False,
                "",
                0.8
            ]
        },
        "seed": {
            "args": [
                -1,
                False,
                -1,
                0,
                0,
                0
            ]
        },
        "controlnet": {
            "args": [
                {
                    "enabled": True,
                    "module": "none",
                    "model": "control_v11p_sd15_canny",
                    "weight": 1,
                    "image": {
                        "image": "",
                        "mask": ""
                    },
                    "resize_mode": "Crop and Resize",
                    "low_vram": False,
                    "processor_res": 512,
                    "threshold_a": 100,
                    "threshold_b": 200,
                    "guidance_start": 0,
                    "guidance_end": 1,
                    "pixel_perfect": True,
                    "control_mode": "Balanced",
                    "save_detected_map": True,
                    "is_ui": False,
                    "input_mode": "simple",
                    "batch_images": "",
                    "output_dir": "",
                    "loopback": False
                }
            ]
        },
        "extra options": {
            "args": []
        }
    }
}
