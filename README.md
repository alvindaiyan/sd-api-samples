## 文生图及图生图代码示例:

下载代码, 根据图中填入自己的api url和token:

```python
    
    # python-samples/main.py:
    sample_client = PythonAPISamples(
        api_url='https://{api-gateway}.execute-api.{region}.amazonaws.com/prod/',
        api_token='token',
        user_id='flash'
    )
```

运行python, 脚本:

```
python main.py
```

查看结果:

```shell
    (venv) (base) ➜  python-samples git:(main) ✗ tree output 
    output
    ├── img2img
    │   ├── metadata_d6f94edb-6654-47c8-aeac-b6a6b6394567.json
    │   ├── result_d6f94edb-6654-47c8-aeac-b6a6b6394567_0.png
    │   └── result_d6f94edb-6654-47c8-aeac-b6a6b6394567_1.png
    └── txt2img
        ├── metadata_5fb204de-cf58-45da-8dfb-8fa081253255.json
        ├── result_5fb204de-cf58-45da-8dfb-8fa081253255_0.png
        └── result_5fb204de-cf58-45da-8dfb-8fa081253255_1.png
    
    2 directories, 6 files
```
