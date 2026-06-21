optimizer = dict(type='SGD', lr=0.0002, momentum=0.9, weight_decay=0.0005)
optim_wrapper = dict(type='OptimWrapper', optimizer=optimizer, clip_grad=dict(max_norm=35, norm_type=2))

param_scheduler = [
    dict(type='PolyLR', eta_min=1e-5, power=0.9, begin=0, end=15, by_epoch=True),
]

train_cfg = dict(type='EpochBasedTrainLoop', max_epochs=15)
val_cfg = dict(type='ValLoop')
test_cfg = dict(type='TestLoop')


default_hooks = dict(
    timer=dict(type='IterTimerHook'),
    logger=dict(type='LoggerHook', interval=20),
    param_scheduler=dict(type='ParamSchedulerHook'),
    checkpoint=dict(type='CheckpointHook', by_epoch=True, interval=1),
    sampler_seed=dict(type='DistSamplerSeedHook'),
    visualization=dict(type='SegVisualizationHook', interval=1, draw=True)
)