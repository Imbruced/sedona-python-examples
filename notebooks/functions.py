from typing import List
from shapely.geometry import MultiPolygon
from shapely.geometry import Polygon
from shapely.geometry import Point

def create_grid(rows: int, cols: int, grid_size: float, origin_x:float, origin_y:float) -> List:
    grids = []
    for r in range(rows):
        for c in range(cols):
            polygon = Polygon(
                    [
                        Point(c*grid_size+origin_x, r*grid_size+origin_y),
                        Point(c*grid_size+origin_x, (r+1)*grid_size+origin_y),
                        Point((c+1)*grid_size+origin_x, (r+1)*grid_size+origin_y),
                        Point((c+1)*grid_size+origin_x, r*grid_size+origin_y),
                        Point(c*grid_size+origin_x, r*grid_size+origin_y)
                    ]
                    
                )
            grids.append(
                polygon
            )
    return MultiPolygon(grids)
            
