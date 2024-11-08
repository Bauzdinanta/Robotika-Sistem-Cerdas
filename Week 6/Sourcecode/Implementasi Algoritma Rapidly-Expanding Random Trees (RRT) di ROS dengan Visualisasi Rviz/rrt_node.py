#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point, PoseStamped
from visualization_msgs.msg import Marker, MarkerArray
from nav_msgs.msg import Path
import random
import math
import numpy as np

class RRTNode:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

class RRTPlanner(Node):
    def __init__(self):
        super().__init__('rrt_planner')
        
        # Parameters
        self.max_iterations = 5000
        self.step_size = 0.5
        self.goal_sample_rate = 0.1
        self.min_dist_to_goal = 0.5
        
        # Start and goal positions
        self.start = RRTNode(0.0, 0.0)
        self.goal = RRTNode(10.0, 10.0)
        self.nodes = [self.start]
        
        # Publishers
        self.marker_pub = self.create_publisher(MarkerArray, 'visualization_marker_array', 10)
        self.path_pub = self.create_publisher(Path, 'rrt_path', 10)
        
        # Timer for visualization updates
        self.timer = self.create_timer(0.1, self.visualization_callback)
        
        # Start planning
        self.plan_path()

    def plan_path(self):
        for i in range(self.max_iterations):
            if random.random() < self.goal_sample_rate:
                rnd = RRTNode(self.goal.x, self.goal.y)
            else:
                rnd = RRTNode(
                    random.uniform(-15, 15),
                    random.uniform(-15, 15)
                )
            
            nearest_node = self.get_nearest_node(rnd)
            new_node = self.steer(nearest_node, rnd)
            
            if new_node and not self.check_collision(nearest_node, new_node):
                self.nodes.append(new_node)
                new_node.parent = nearest_node
                
                if self.dist(new_node, self.goal) < self.min_dist_to_goal:
                    final_node = RRTNode(self.goal.x, self.goal.y)
                    final_node.parent = new_node
                    self.nodes.append(final_node)
                    self.get_logger().info('Path found!')
                    return True
        
        self.get_logger().warning('Could not find path!')
        return False

    def get_nearest_node(self, rnd_node):
        distances = [(node.x - rnd_node.x) ** 2 + (node.y - rnd_node.y) ** 2 
                    for node in self.nodes]
        nearest_idx = distances.index(min(distances))
        return self.nodes[nearest_idx]

    def steer(self, from_node, to_node):
        dist = self.dist(from_node, to_node)
        if dist < self.step_size:
            return to_node
        
        theta = math.atan2(to_node.y - from_node.y, 
                          to_node.x - from_node.x)
        new_node = RRTNode(
            from_node.x + self.step_size * math.cos(theta),
            from_node.y + self.step_size * math.sin(theta)
        )
        return new_node

    def dist(self, node1, node2):
        return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)

    def check_collision(self, node1, node2):
        # Implement obstacle checking here if needed
        return False

    def visualization_callback(self):
        marker_array = MarkerArray()
        
        # Nodes marker
        nodes_marker = Marker()
        nodes_marker.header.frame_id = "map"
        nodes_marker.header.stamp = self.get_clock().now().to_msg()
        nodes_marker.ns = "nodes"
        nodes_marker.id = 0
        nodes_marker.type = Marker.POINTS
        nodes_marker.action = Marker.ADD
        nodes_marker.pose.orientation.w = 1.0
        nodes_marker.scale.x = 0.1
        nodes_marker.scale.y = 0.1
        nodes_marker.color.r = 1.0
        nodes_marker.color.a = 1.0
        
        # Edges marker
        edges_marker = Marker()
        edges_marker.header.frame_id = "map"
        edges_marker.header.stamp = self.get_clock().now().to_msg()
        edges_marker.ns = "edges"
        edges_marker.id = 1
        edges_marker.type = Marker.LINE_LIST
        edges_marker.action = Marker.ADD
        edges_marker.pose.orientation.w = 1.0
        edges_marker.scale.x = 0.02
        edges_marker.color.g = 1.0
        edges_marker.color.a = 1.0

        # Add nodes and edges to markers
        for node in self.nodes:
            point = Point()
            point.x = node.x
            point.y = node.y
            nodes_marker.points.append(point)
            
            if node.parent:
                point_parent = Point()
                point_parent.x = node.parent.x
                point_parent.y = node.parent.y
                edges_marker.points.append(point_parent)
                edges_marker.points.append(point)

        marker_array.markers = [nodes_marker, edges_marker]
        self.marker_pub.publish(marker_array)
        
        # Publish path
        if len(self.nodes) > 0 and self.nodes[-1].x == self.goal.x and self.nodes[-1].y == self.goal.y:
            path = Path()
            path.header.frame_id = "map"
            path.header.stamp = self.get_clock().now().to_msg()
            
            current = self.nodes[-1]
            while current is not None:
                pose = PoseStamped()
                pose.pose.position.x = current.x
                pose.pose.position.y = current.y
                path.poses.insert(0, pose)
                current = current.parent
            
            self.path_pub.publish(path)

def main(args=None):
    rclpy.init(args=args)
    rrt_planner = RRTPlanner()
    rclpy.spin(rrt_planner)
    rrt_planner.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
