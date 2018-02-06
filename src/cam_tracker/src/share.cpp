/*

g++ -o position-client-example -Wall -ansi -pedantic -O3 position-client-example.cpp -lboost_system -lpthread -std=c++11

*/
#include <roscpp.h>
#include <iostream>
#include <string>
#include <cstdlib>
#include <chrono>
#include <thread>
#include <iomanip>
#include <vector>
#include <iterator>

#include <boost/asio.hpp>

struct Point {
  double x,y;
};



class Share {

 //  if(argc!=3) {
 //    std::cerr << "Usage : " << argv[0] 
	//       << " <hostname> <port> " << std::endl;
 //    return 1;
 //  }

 //  std::string hostname = argv[1];
 //  std::string port     = argv[2]; // port is a string like "10000"
 //  std::chrono::duration<int,std::milli> pause_duration(500);
  
 //  try {
 //    // Let us create a stream and handle it with exceptions.
 //    boost::asio::ip::tcp::iostream socket;
 //    socket.exceptions(std::ios::failbit | std::ios::badbit | std::ios::eofbit);

 //    // Let us connect the client socket.
 //    socket.connect(hostname,port);

 //    std::cout << "I set persistance to 15s" << std::endl;
 //    socket << "persistance " << 15 << std::endl;

 //    std::cout << "Every 500ms I sent one point." << std::endl;
 //    for(unsigned i=0; i < 20; ++i) {  
 //      double x = i;
 //      double y = x*x;
 //      socket << "put " << x << ' ' << y << std::endl;
 //      std::cout << "  Point " << std::setw(2) << i+1 << "/20 sent.   \r" << std::flush;
 //      std::this_thread::sleep_for(pause_duration);
 //    }
 //    std::cout << std::endl;

    
 //    std::cout << "Every 500ms I read the points, until the server is empty" << std::endl;
 //    std::vector<Point> points;
 //    unsigned int nb;
    
 //    socket << "get" << std::endl;
 //    socket >> nb;
 //    while(nb != 0) {
 //      points.clear();
 //      auto out = std::back_inserter(points);
 //      double x,y;
 //      for(unsigned int i = 0; i < nb; ++i) {
	// socket >> x >> y;
	// *(out++) = {x,y};  // Appends the point to points.
 //      }
      
 //      std::cout << "  " << std::setw(2) << nb << " points got" << std::endl;
 //      std::this_thread::sleep_for(pause_duration);
 //      socket << "get" << std::endl;
 //      socket >> nb;
 //    }
    
 //  }			    
 //  catch(std::exception& e) {
 //    std::cerr << "Exception caught : " << e.what() << std::endl;
 //  }

  return 0;
}


int main(int argc, char * argv[]) 
{
    ros::init(argc,argv,"share");

    CollisionAvoidance ca;

    ros::spin();
    // TODO: implement a security layer
}
