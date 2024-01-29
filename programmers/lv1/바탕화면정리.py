def solution(wallpaper):
    answer = []
    # print(wallpaper)

    files = []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                files.append((i, j))
    
    # print(files)
    lux = files[0][0]
    
    y_coords = []
    x_coords = []
    for f in files:
        y_coords.append(f[1])
        x_coords.append(f[0])

    luy = min(y_coords)
    rdy = max(y_coords) + 1
    rdx = max(x_coords) + 1
    # rdx : 
    # rdy :
    return [lux, luy, rdx, rdy]

# left top = 0,0

print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."]))