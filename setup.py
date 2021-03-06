'''
Created on 30.12.2018

@author: ED
'''
import setuptools
from PyTrinamic.version import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTrinamic",
    version=__version__,
    author="ED, LK, LH, JM, ..",
    author_email="tmc_info@trinamic.com",
    description="TRINAMIC's Python Technology Access Package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trinamic/PyTrinamic",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "python-can>=3,<4",
        "canopen",
        "pyserial>=3"
    ],
    py_modules=[
        "PyTrinamic/connections/connection_interface",
        "PyTrinamic/connections/ConnectionManager",
        "PyTrinamic/connections/dummy_tmcl_interface",
        "PyTrinamic/connections/pcan_tmcl_interface",
        "PyTrinamic/connections/socketcan_tmcl_interface",
        "PyTrinamic/connections/serial_tmcl_interface",
        "PyTrinamic/connections/tmcl_interface",
        "PyTrinamic/connections/uart_ic_interface",
        "PyTrinamic/connections/usb_tmcl_interface",
        "PyTrinamic/connections/CANopen_interface",
        "PyTrinamic/connections/pcan_CANopen_interface",
        "PyTrinamic/evalboards/eval_interface",
        "PyTrinamic/evalboards/TMC2041_eval",
        "PyTrinamic/evalboards/TMC2100_eval",
        "PyTrinamic/evalboards/TMC2130_eval",
        "PyTrinamic/evalboards/TMC2160_eval",
        "PyTrinamic/evalboards/TMC2208_eval",
        "PyTrinamic/evalboards/TMC2209_eval",
        "PyTrinamic/evalboards/TMC2224_eval",
        "PyTrinamic/evalboards/TMC2225_eval",
        "PyTrinamic/evalboards/TMC2300_eval",
        "PyTrinamic/evalboards/TMC2590_eval",
        "PyTrinamic/evalboards/TMC2660_eval",
        "PyTrinamic/evalboards/TMC4361_eval",
        "PyTrinamic/evalboards/TMC4671_eval",
        "PyTrinamic/evalboards/TMC5031_eval",
        "PyTrinamic/evalboards/TMC5041_eval",
        "PyTrinamic/evalboards/TMC5062_eval",
        "PyTrinamic/evalboards/TMC5072_eval",
        "PyTrinamic/evalboards/TMC5130_eval",
        "PyTrinamic/evalboards/TMC5160_eval",
        "PyTrinamic/evalboards/TMC5160_shield",
        "PyTrinamic/evalboards/TMC5161_eval",
        "PyTrinamic/evalboards/TMC6100_eval",
        "PyTrinamic/evalboards/TMC6200_eval",
        "PyTrinamic/evalboards/TMC7300_eval",
        "PyTrinamic/ic/ic_interface",
        "PyTrinamic/ic/TMC2041/TMC2041_fields",
        "PyTrinamic/ic/TMC2041/TMC2041_register_variant",
        "PyTrinamic/ic/TMC2041/TMC2041_register",
        "PyTrinamic/ic/TMC2041/TMC2041",
        "PyTrinamic/ic/TMC2100/TMC2100_fields",
        "PyTrinamic/ic/TMC2100/TMC2100_register_variant",
        "PyTrinamic/ic/TMC2100/TMC2100_register",
        "PyTrinamic/ic/TMC2100/TMC2100",
        "PyTrinamic/ic/TMC2130/TMC2130_fields",
        "PyTrinamic/ic/TMC2130/TMC2130_register_variant",
        "PyTrinamic/ic/TMC2130/TMC2130_register",
        "PyTrinamic/ic/TMC2130/TMC2130",
        "PyTrinamic/ic/TMC2160/TMC2160_fields",
        "PyTrinamic/ic/TMC2160/TMC2160_register_variant",
        "PyTrinamic/ic/TMC2160/TMC2160_register",
        "PyTrinamic/ic/TMC2160/TMC2160",
        "PyTrinamic/ic/TMC2208/TMC2208_fields",
        "PyTrinamic/ic/TMC2208/TMC2208_register_variant",
        "PyTrinamic/ic/TMC2208/TMC2208_register",
        "PyTrinamic/ic/TMC2208/TMC2208",
        "PyTrinamic/ic/TMC2209/TMC2209_fields",
        "PyTrinamic/ic/TMC2209/TMC2209_register_variant",
        "PyTrinamic/ic/TMC2209/TMC2209_register",
        "PyTrinamic/ic/TMC2209/TMC2209",
        "PyTrinamic/ic/TMC2224/TMC2224_fields",
        "PyTrinamic/ic/TMC2224/TMC2224_register_variant",
        "PyTrinamic/ic/TMC2224/TMC2224_register",
        "PyTrinamic/ic/TMC2224/TMC2224",
        "PyTrinamic/ic/TMC2225/TMC2225_fields",
        "PyTrinamic/ic/TMC2225/TMC2225_register_variant",
        "PyTrinamic/ic/TMC2225/TMC2225_register",
        "PyTrinamic/ic/TMC2225/TMC2225",
        "PyTrinamic/ic/TMC2300/TMC2300_fields",
        "PyTrinamic/ic/TMC2300/TMC2300_register_variant",
        "PyTrinamic/ic/TMC2300/TMC2300_register",
        "PyTrinamic/ic/TMC2300/TMC2300",
        "PyTrinamic/ic/TMC2590/TMC2590_fields",
        "PyTrinamic/ic/TMC2590/TMC2590_register_variant",
        "PyTrinamic/ic/TMC2590/TMC2590_register",
        "PyTrinamic/ic/TMC2590/TMC2590",
        "PyTrinamic/ic/TMC2660/TMC2660_fields",
        "PyTrinamic/ic/TMC2660/TMC2660_register_variant",
        "PyTrinamic/ic/TMC2660/TMC2660_register",
        "PyTrinamic/ic/TMC2660/TMC2660",
        "PyTrinamic/ic/TMC4330/TMC4330_fields",
        "PyTrinamic/ic/TMC4330/TMC4330_register_variant",
        "PyTrinamic/ic/TMC4330/TMC4330_register",
        "PyTrinamic/ic/TMC4330/TMC4330",
        "PyTrinamic/ic/TMC4331/TMC4331_fields",
        "PyTrinamic/ic/TMC4331/TMC4331_register_variant",
        "PyTrinamic/ic/TMC4331/TMC4331_register",
        "PyTrinamic/ic/TMC4331/TMC4331",
        "PyTrinamic/ic/TMC4361/TMC4361_fields",
        "PyTrinamic/ic/TMC4361/TMC4361_register_variant",
        "PyTrinamic/ic/TMC4361/TMC4361_register",
        "PyTrinamic/ic/TMC4361/TMC4361",
        "PyTrinamic/ic/TMC4671/TMC4671_fields",
        "PyTrinamic/ic/TMC4671/TMC4671_register_variant",
        "PyTrinamic/ic/TMC4671/TMC4671_register",
        "PyTrinamic/ic/TMC4671/TMC4671",
        "PyTrinamic/ic/TMC5031/TMC5031_fields",
        "PyTrinamic/ic/TMC5031/TMC5031_register_variant",
        "PyTrinamic/ic/TMC5031/TMC5031_register",
        "PyTrinamic/ic/TMC5031/TMC5031",
        "PyTrinamic/ic/TMC5041/TMC5041_fields",
        "PyTrinamic/ic/TMC5041/TMC5041_register_variant",
        "PyTrinamic/ic/TMC5041/TMC5041_register",
        "PyTrinamic/ic/TMC5041/TMC5041",
        "PyTrinamic/ic/TMC5062/TMC5062_fields",
        "PyTrinamic/ic/TMC5062/TMC5062_register_variant",
        "PyTrinamic/ic/TMC5062/TMC5062_register",
        "PyTrinamic/ic/TMC5062/TMC5062",
        "PyTrinamic/ic/TMC5072/TMC5072_fields",
        "PyTrinamic/ic/TMC5072/TMC5072_register_variant",
        "PyTrinamic/ic/TMC5072/TMC5072_register",
        "PyTrinamic/ic/TMC5072/TMC5072",
        "PyTrinamic/ic/TMC5130/TMC5130_fields",
        "PyTrinamic/ic/TMC5130/TMC5130_register_variant",
        "PyTrinamic/ic/TMC5130/TMC5130_register",
        "PyTrinamic/ic/TMC5130/TMC5130",
        "PyTrinamic/ic/TMC5160/TMC5160_fields",
        "PyTrinamic/ic/TMC5160/TMC5160_register_variant",
        "PyTrinamic/ic/TMC5160/TMC5160_register",
        "PyTrinamic/ic/TMC5160/TMC5160",
        "PyTrinamic/ic/TMC5161/TMC5161_fields",
        "PyTrinamic/ic/TMC5161/TMC5161_register_variant",
        "PyTrinamic/ic/TMC5161/TMC5161_register",
        "PyTrinamic/ic/TMC5161/TMC5161",
        "PyTrinamic/ic/TMC6100/TMC6100_fields",
        "PyTrinamic/ic/TMC6100/TMC6100_register_variant",
        "PyTrinamic/ic/TMC6100/TMC6100_register",
        "PyTrinamic/ic/TMC6100/TMC6100",
        "PyTrinamic/ic/TMC6200/TMC6200_fields",
        "PyTrinamic/ic/TMC6200/TMC6200_register_variant",
        "PyTrinamic/ic/TMC6200/TMC6200_register",
        "PyTrinamic/ic/TMC6200/TMC6200",
        "PyTrinamic/ic/TMC7300/TMC7300_fields",
        "PyTrinamic/ic/TMC7300/TMC7300_register_variant",
        "PyTrinamic/ic/TMC7300/TMC7300_register",
        "PyTrinamic/ic/TMC7300/TMC7300",
        "PyTrinamic/modules/TMC_EvalShield",
        "PyTrinamic/modules/TMC603/TMC_603",
        "PyTrinamic/modules/TMCC160/TMCC_160",
        "PyTrinamic/modules/TMCM0010OPC/TMCM_0010_OPC",
        "PyTrinamic/modules/TMCM1160/TMCM_1160",
        "PyTrinamic/modules/TMCM1161/TMCM_1161",
        "PyTrinamic/modules/TMCM1270/TMCM_1270",
        "PyTrinamic/modules/TMCM1276/TMCM_1276",
        "PyTrinamic/modules/TMCM1617/TMCM_1617",
        "PyTrinamic/modules/TMCM1630/TMCM_1630",
        "PyTrinamic/modules/TMCM1633/TMCM_1633",
        "PyTrinamic/modules/TMCM1636/TMCM_1636",
        "PyTrinamic/modules/TMCM1640/TMCM_1640",
        "PyTrinamic/modules/TMCM1670/TMCM_1670",
        "PyTrinamic/modules/TMCM6212/TMCM_6212",
        "PyTrinamic/helpers",
        "PyTrinamic/version",
        "PyTrinamic/features/Feature",
        "PyTrinamic/features/StallGuard",
        "PyTrinamic/features/CoolStep",
    ],
    scripts=[
        "PyTrinamic/examples/evalboards/TMC2041/TMC2041_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2041/TMC2041_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2100/TMC2100_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2100/TMC2100_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2130/TMC2130_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2130/TMC2130_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2160/TMC2160_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2160/TMC2160_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2208/TMC2208_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2208/TMC2208_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2209/TMC2209_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2209/TMC2209_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2224/TMC2224_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2224/TMC2224_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2225/TMC2225_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2225/TMC2225_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2300/TMC2300_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2300/TMC2300_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2590/TMC2590_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2590/TMC2590_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2660/TMC2660_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2660/TMC2660_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC4331/TMC4331_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC4331/TMC4331_eval_TMC2130_eval_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC4330/TMC4330_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC4330/TMC4330_eval_TMC2160_eval_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC4361/TMC4361_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC4361/TMC4361_eval_TMC2660_eval_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_BLDC_ABN_encoder_offset_estimation.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_BLDC_ABN_encoder.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_BLDC_open_loop.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_TMC6100_eval_BLDC_ABN_encoder.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_TMC6100_eval_BLDC_open_loop.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_TMC6200_eval_BLDC_ABN_encoder.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_TMC6200_eval_BLDC_open_loop.py",
        "PyTrinamic/examples/evalboards/TMC5031/TMC5031_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5031/TMC5031_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC5031/TMC5031_stallGuardDemo.py",
        "PyTrinamic/examples/evalboards/TMC5041/TMC5041_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5041/TMC5041_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC5041/TMC5041_stallGuardDemo.py",
        "PyTrinamic/examples/evalboards/TMC5062/TMC5062_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5062/TMC5062_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC5072/TMC5072_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5072/TMC5072_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC5130/TMC5130_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5130/TMC5130_MicroStep.py",
        "PyTrinamic/examples/evalboards/TMC5160/TMC5160_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5160/TMC5160_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC5160_shield/TMC5160_shield_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5160_shield/TMC5160_coolStep_demo.py",
        "PyTrinamic/examples/evalboards/TMC5160_shield/TMC5160_stallGuard_demo.py",
        "PyTrinamic/examples/evalboards/TMC5160_shield/TMC5160_coolStep_demo_min.py",
        "PyTrinamic/examples/evalboards/TMC5160_shield/TMC5160_stallGuard_demo_min.py",
        "PyTrinamic/examples/evalboards/TMC5161/TMC5161_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5161/TMC5161_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC7300/TMC7300_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC7300/TMC7300_rotateDemo.py",
        "PyTrinamic/examples/modules/TMC_603/TMC_603_TMCL_encoder_analog_input_test.py",
        "PyTrinamic/examples/modules/TMC_603/TMC_603_TMCL_encoder_positioning_test.py",
        "PyTrinamic/examples/modules/TMC_603/TMC_603_TMCL_hall_digital_input_test.py",
        "PyTrinamic/examples/modules/TMC_603/TMC_603_TMCL_hall_positioning_test.py",
        "PyTrinamic/examples/modules/TMCC_160/TMCC_160_TMCL_foc_encoder_positioning_test.py",
        "PyTrinamic/examples/modules/TMCC_160/TMCC_160_TMCL_foc_hall_digital_analog_input_test.py",
        "PyTrinamic/examples/modules/TMCM_0010_OPC/TMCM_0010_TMCL_OPC_config_check.py",
        "PyTrinamic/examples/modules/TMCM_0010_OPC/TMCM_0010_TMCL_OPC_config_update.py",
        "PyTrinamic/examples/modules/TMCM_1160/TMCM_1160_TMCL_rotateDemo.py",
        "PyTrinamic/examples/modules/TMCM_1160/TMCM_1160_CANopen_PP_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1160/TMCM_1160_CANopen_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1161/TMCM_1161_TMCL_rotateDemo.py",
        "PyTrinamic/examples/modules/TMCM_1270/TMCM_1270_CANopen_PP_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1270/TMCM_1270_CANopen_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1270/TMCM_1270_TMCL_rotateDemo.py",
        "PyTrinamic/examples/modules/TMCM_1276/TMCM_1276_CANopen_PP_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1276/TMCM_1276_CANopen_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1276/TMCM_1276_TMCL_rotateDemo.py",
        "PyTrinamic/examples/modules/TMCM_1617/TMCM_1617_TMCL_encoder_positioning_test.py",
        "PyTrinamic/examples/modules/TMCM_1617/TMCM_1617_TMCL_hall_digital_input_test.py",
        "PyTrinamic/examples/modules/TMCM_1617/TMCM_1617_TMCL_hall_positioning_test.py",
        "PyTrinamic/examples/modules/TMCM_1630/TMCM_1630_TMCL_encoder_analog_input_test.py",
        "PyTrinamic/examples/modules/TMCM_1630/TMCM_1630_TMCL_encoder_positioning_test.py",
        "PyTrinamic/examples/modules/TMCM_1630/TMCM_1630_TMCL_hall_digital_input_test.py",
        "PyTrinamic/examples/modules/TMCM_1630/TMCM_1630_TMCL_hall_positioning_test.py",
        "PyTrinamic/examples/modules/TMCM_1633/TMCM_1633_TMCL_encoder_limit_switches.py",
        "PyTrinamic/examples/modules/TMCM_1633/TMCM_1633_TMCL_hall_limit_switches.py",
        "PyTrinamic/examples/modules/TMCM_1636/TMCM_1636_TMCL_position_abn_abs.py",
        "PyTrinamic/examples/modules/TMCM_1636/TMCM_1636_TMCL_rotate_hall_endstop.py",
        "PyTrinamic/examples/modules/TMCM_1636/TMCM_1636_TMCL_rotate_hall.py",
        "PyTrinamic/examples/modules/TMCM_1636/TMCM_1636_TMCL_rotate_openloop.py",
        "PyTrinamic/examples/modules/TMCM_1640/TMCM_1640_TMCL_encoder_analog_input_test.py",
        "PyTrinamic/examples/modules/TMCM_1640/TMCM_1640_TMCL_encoder_positioning_test.py",
        "PyTrinamic/examples/modules/TMCM_1640/TMCM_1640_TMCL_hall_digital_input_test.py",
        "PyTrinamic/examples/modules/TMCM_1640/TMCM_1640_TMCL_hall_positioning_test.py",
        "PyTrinamic/examples/modules/TMCM_1670/TMCM_1670_TMCL_encoder_n_channel.py",
        "PyTrinamic/examples/modules/TMCM_1670/TMCM_1670_TMCL_limit_switches.py",
        "PyTrinamic/examples/modules/TMCM_1670/TMCM_1670_TMCL_positioning.py",
        "PyTrinamic/examples/modules/TMCM_6212/TMCM_6212_TMCL_rotateDemo.py",
        "PyTrinamic/examples/tools/FirmwareUpdate.py",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    zip_safe=False,
)
