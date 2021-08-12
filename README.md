# micro-computer

Made with CocoRobo X-AI Module, built on MaixPy (MicroPython).

![hor](https://user-images.githubusercontent.com/1622557/129134259-f42cbc47-d570-4943-a2ac-6103d11e92ea.jpg)

- For specs: https://tjtl.io/Startup (scroll down to the __The 2nd Generation: “CocoRobo X”__ section.)
- To program:
  - MaixPy IDE: https://wiki.sipeed.com/soft/maixpy/zh/get_started/env_maixpyide.html?highlight=ide
  - CocoBlockly X, Block Mode: https://x.cocorobo.cn
  - CocoBlockly X, Code Mode: https://x.cocorobo.cn/python
- To learn:
  - MaixPy Docs: https://wiki.sipeed.com/soft/maixpy/zh/
  - Blockly for X-AI Module Docs: https://x-help.cocorobo.cn
- Burning firmware:
  - To be edited.

---

## Additional comments:

To create customized font from common font file (`.otf`, `.ttf`, etc.) to `.Dzk`, read [here](https://github.com/sipeed/MaixPy_scripts/blob/8407d0eb96fd076f606f6db62cc766135a7c8416/multimedia/gui/image/demo_draw_font/readme.md) for more information.

To use customized font based on the `3type` version of the CocoRobo X Module firmware, read `custom-font-display.py`.
1. Go to `https://x.cocorobo.cn/python`
2. Paste the code from `custom-font-display.py` to the code area of the loaded page
3. Click `Run` to see the output immidiately. Or click `Upload` to upload this code file to the module, you can run the uploaded code by clicking the `Run Last` button on the bootup interface.