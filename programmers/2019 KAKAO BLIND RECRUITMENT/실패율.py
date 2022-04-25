def solution(N, stages):
    stage_fail_cnt=dict()
    stage_enter_cnt=dict()
    for stage in range(1, N+1):
        stage_fail_cnt[stage]=0
        stage_enter_cnt[stage]=0
    for stage in stages:
        if stage != N+1:
            stage_fail_cnt[stage]+=1
        for i in range(1, min(stage+1, N+1)):
            stage_enter_cnt[i]+=1

    stage_fail_rate=dict()
    for stage in range(1, N+1):
        if stage_enter_cnt[stage] == 0:
            stage_fail_rate[stage] = 0
        else:
            stage_fail_rate[stage] = stage_fail_cnt[stage]/stage_enter_cnt[stage]

    fail_rate_stage=dict()
    for fail_rate in stage_fail_rate.values():
        fail_rate_stage[fail_rate]=[]
    for stage,fail_rate in stage_fail_rate.items():
        fail_rate_stage[fail_rate].append(stage)

    answer = []
    fail_cnts = list(fail_rate_stage.keys())
    fail_cnts.sort(reverse=True)

    for fail_rate in fail_cnts:
        answer += sorted(fail_rate_stage[fail_rate])

    return answer

inputs=[
    [5 , [2, 1, 2, 6, 2, 4, 3, 3]],    #[3,4,2,1,5]
    [4,	[4,4,4,4,4]]	#[4,1,2,3]
]

for input in inputs:
    print(solution(input[0], input[1]))