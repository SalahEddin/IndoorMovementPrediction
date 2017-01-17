paths = [
    'BCADFJI',
    'IJMQRST',
    'TSRQMJI',
    'IJMQRSVX',
    'XVSRQJI',
    'IJMQUW',
    'WUQMJI',
    'IJFDACB'
]

partialPath = 'WU'
time = 16  # 9 -16


def get_next_step(thePath, time):
    paths_fully_matching = [
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False
    ]
    # exact match
    found_count = 0
    for idx, path in enumerate(paths):
        if thePath in path:
            paths_fully_matching[idx] = True
            found_count += 1

    # if only only one is found, then print it with 1.0 probability
    if sum(paths_fully_matching) == 1:
        for i, v in enumerate(paths_fully_matching):
            if v is True:
                print('100% probability of next step: ' + paths[i].split(thePath)[1][0])
    elif sum(paths_fully_matching) == 0:
        if len(thePath) <= 1:
            print('No pattern was matched')
        else:
            get_next_step(thePath[1:], time)
    else:
        # get the closest time

        # initialise with max length
        prevLength = len(paths)
        nextStep = ''
        for i,v in enumerate(paths_fully_matching):
            if paths_fully_matching[i] is True and abs((i+9)-time) <= prevLength:
                nextStep = paths[i].split(thePath)[1][0]
                prevLength = (abs((i+9)-time))
        print('highest probability of next step: ' + nextStep)

get_next_step(partialPath, time)
