#include <iostream>
using namespace std;

#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>     // Basic OpenCV structures (cv::Mat)
// using namespace cv;

int main() {
    cv::Mat img = cv::imread("girl_xinh.jpg", cv::IMREAD_COLOR);
    
    cout << "img.step " << img.step << endl;
    cout << "img.channels() " << img.channels() << endl;
    
    for(int row=0; row<img.rows; row++) {
        for(int col=0; col<img.cols; col++) {
            //*(img.ptr(row, col)) = 0;
            uchar *ptr = img.ptr(row, col);
            *ptr = 0;
            *(ptr+2) = 0;
        }
    }
    
    cv::imwrite("girl_xinh_yellow.jpg", img);
}