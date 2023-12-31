img2img_param = {
    "prompt": "warrior, man, bald",
    "negative_prompt": "bad quality",
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
    "denoising_strength": 0.75,
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
    "init_images": [],
    "resize_mode": 0,
    "image_cfg_scale": 1.5,
    "mask": None,
    "mask_blur_x": 4,
    "mask_blur_y": 4,
    "mask_blur": None,
    "inpainting_fill": 1,
    "inpaint_full_res": False,
    "inpaint_full_res_padding": 32,
    "inpainting_mask_invert": 0,
    "initial_noise_multiplier": 1.0,
    "latent_mask": None,
    "sampler_index": "DPM++ 2M Karras",
    "include_init_images": False,
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
                    "module": "canny",
                    "model": "control_v11p_sd15_canny",
                    "weight": 1,
                    "image": None,
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
                    "is_ui": True,
                    "input_mode": "simple",
                    "batch_images": "",
                    "output_dir": "",
                    "loopback": False
                },
                {
                    "enabled": False,
                    "module": "none",
                    "model": "None",
                    "weight": 1,
                    "image": None,
                    "resize_mode": "Crop and Resize",
                    "low_vram": False,
                    "processor_res": -1,
                    "threshold_a": -1,
                    "threshold_b": -1,
                    "guidance_start": 0,
                    "guidance_end": 1,
                    "pixel_perfect": False,
                    "control_mode": "Balanced",
                    "save_detected_map": True,
                    "is_ui": True,
                    "input_mode": "simple",
                    "batch_images": "",
                    "output_dir": "",
                    "loopback": False
                },
                {
                    "enabled": False,
                    "module": "none",
                    "model": "None",
                    "weight": 1,
                    "image": None,
                    "resize_mode": "Crop and Resize",
                    "low_vram": False,
                    "processor_res": -1,
                    "threshold_a": -1,
                    "threshold_b": -1,
                    "guidance_start": 0,
                    "guidance_end": 1,
                    "pixel_perfect": False,
                    "control_mode": "Balanced",
                    "save_detected_map": True,
                    "is_ui": True,
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

