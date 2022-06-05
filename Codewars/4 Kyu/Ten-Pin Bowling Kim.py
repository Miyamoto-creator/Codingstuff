def bowling_score(frames):
    arr = frames.split()
    arr = [ arr[i].rjust(2, '-') for i in range(0,len(arr))]
    arr = [char for char in "".join(arr) ]
    print(arr)
    awns = 0
    frame = 0
    for i in range(0,len(arr), 2):
        step, x = 2 ,0
        while x < step:
            if arr[i+x] == "-":
                if x > 1:
                    step += 1
            elif arr[i+x] == "X":
                if x == 0:
                    step = 1
                awns += 10
                if x < 2 and step <3 :
                    step += 2
            elif arr[i+x] == "/":
                awns += 10 - int(arr[i+x-1])
                if x < 2:
                    step += 1
            else:
                awns += int(arr[i+x])
            x += 1
        if frame == 9:
            break
        frame += 1
    return awns

print(bowling_score('X X 11 X X X X X X XXX'))