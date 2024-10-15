from tile import Tile

class Grid:
    tiles = []  

    def __init__(self, pixels_x, pixels_y, pixel_size):
        self.pixels_x = pixels_x
        self.pixels_y = pixels_y
        self.pixel_size = pixel_size   

        self.tiles = [[Tile(x, y, pixel_size, False, False) for x in range(pixels_x) for y in range(pixels_y)]]

    def get_neighbors(self, tile):
        neighbors = []


        # private Point[] GetNeighbors(int[,] map, Point point)
        # {
        #     List<Point> neighbors = new List<Point>();

        #     if (map.GetLength(0) - 1 != point.X)
        #     {
        #         neighbors.Add(new Point(point.X + 1, point.Y));
        #     }

        #     if (point.X != 0)
        #     {
        #         neighbors.Add(new Point(point.X - 1, point.Y));
        #     }

        #     if (map.GetLength(1) - 1 != point.Y)
        #     {
        #         neighbors.Add(new Point(point.X, point.Y + 1));
        #     }

        #     if (point.Y != 0)
        #     {
        #         neighbors.Add(new Point(point.X, point.Y -  1));
        #     }

        #     return neighbors.ToArray();
        # }