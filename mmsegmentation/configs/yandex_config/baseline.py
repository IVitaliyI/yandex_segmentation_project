_base_ = [
    '../_base_/models/deeplabv3_r50-d8.py', 
    '../_base_/datasets/yandex_segementation.py',
    '../_base_/default_runtime.py', 
    '../_base_/schedules/schedule_yandex_seg.py'
]


visualizer = dict(
    type='Visualizer',
    vis_backends=[
        dict(type='LocalVisBackend'),
        dict(
            type='ClearMLVisBackend',
            init_kwargs=dict(
                project_name='YaSprint2',
                task_name='deeplabv3_r50-d8-cats-dogs',
                reuse_last_task_id=False,
                continue_last_task=False,
                output_uri=None,
                auto_connect_arg_parser=True,
                auto_connect_frameworks=True,
                auto_resource_monitoring=True,
                auto_connect_streams=True,
            )
        )     
    ]
)


input_size = (512, 512)
data_preprocessor = dict(size=input_size)
model = dict(
    decode_head=dict(
        num_classes=3,
        loss_decode=dict(
            type='DiceLoss',
            use_sigmoid=False,
            loss_weight=1.0,
        )
    ),
    auxiliary_head=dict(
        num_classes=3,
        loss_decode=dict(
            type='DiceLoss',
            use_sigmoid=False,
            loss_weight=0.4,
        )
    ),
    data_preprocessor=data_preprocessor,
    test_cfg=dict(mode="whole")
)