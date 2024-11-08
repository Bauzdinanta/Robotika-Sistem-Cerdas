#include "rclcpp/rclcpp.hpp"

class PRMNode : public rclcpp::Node {
public:
    PRMNode() : Node("prm_node") {
        RCLCPP_INFO(this->get_logger(), "Probabilistic Roadmap Node Started");
    }
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<PRMNode>());
    rclcpp::shutdown();
    return 0;
}
