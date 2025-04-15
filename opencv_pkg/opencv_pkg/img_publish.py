import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os

class ImgPublish(Node):
    def __init__(self):
        super().__init__('img_publish')
        self.publisher_ = self.create_publisher(Image, 'image_topic', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)  # 10Hz
        self.bridge = CvBridge()

        # image path
        self.img_path = '/home/dori/opencv/img/IU.jpg'
        if not os.path.exists(self.img_path):
            self.get_logger().error(f"Image not found: {self.img_path}")

        self.declare_parameter('width', 640)
        self.width = self.get_parameter('width').value
        self.declare_parameter('length', 480)
        self.length = self.get_parameter('length').value
        output_msg = "Img Width : " + str(self.width) + "\n\r"
        output_msg = output_msg + "Img Length : " + str(self.length)
        self.get_logger().info(output_msg)
 

    def timer_callback(self):
        frame = cv2.imread(self.img_path)
        frame = cv2.resize(frame, (self.width, self.length))
        if frame is not None:
            msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
            self.publisher_.publish(msg)
            self.get_logger().info('Image Successed.')
        else:
            self.get_logger().warning('Failed tocimage.')

def main(args=None):
    rclpy.init(args=args)
    img_publish = ImgPublish()

    try:
        rclpy.spin(img_publish)
    except KeyboardInterrupt:
        pass
    finally:
        img_publish.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
