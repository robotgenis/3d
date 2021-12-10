
/************************************************/
/*  Name:  Brandon Young    Date:  11/14/21     */
/*  Seat:  20    File:  APP_C31_1.cpp           */
/*  Instructor:  PAC 08:00                      */
/************************************************/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <cstdlib>
#include <time.h>
#include <unistd.h>


//Vector structure to handle points and vectors
struct Vector3{
	//3 axis of vector
	float x, y, z;

	//opertator to be able to add vectors
	Vector3 operator+(const Vector3& e){
		Vector3 ret;
		//add each axis of vectors
		ret.x = x + e.x;
		ret.y = y + e.y;
		ret.z = z + e.z;
		//return vector
		return ret;
	}
	//operator to be able to subtract vectros
	Vector3 operator-(const Vector3& e){
		Vector3 ret;
		//add each axis of vector
		ret.x = x - e.x;
		ret.y = y - e.y;
		ret.z = z - e.z;
		//return vector
		return ret;
	}
	//pritn out vector, used for debugging
	void print(){
		printf("<%.4f, %.4f, %.4f>\n", x, y, z);
	}
};

//Rotation matrix object to store a rotation matrix
struct RotationMatrix{
	//matrix variable storing rotation matrix
	float rot[3][3];
	Vector3 applyTo(Vector3 vec){
		Vector3 ret;
		//apply rotation matrix to vector
		ret.x = rot[0][0] * vec.x + rot[0][1] * vec.y + rot[0][2] * vec.z;
		ret.y = rot[1][0] * vec.x + rot[1][1] * vec.y + rot[1][2] * vec.z;
		ret.z = rot[2][0] * vec.x + rot[2][1] * vec.y + rot[2][2] * vec.z;
		return ret;
	}
};

//quaternion structure to handle angle fo camera
struct Quaternion{
	//4d of the quaternion vector and w value
	float x, y, z, w;
	//Creating a quaternion from vector Euler rotaiton 
	void fromVector3(Vector3 vec){
		//Calculate trig value for object
		float c0 = cos(vec.x/2);
		float c1 = cos(vec.y/2);
		float c2 = cos(vec.z/2);
		float s0 = sin(vec.x/2);
		float s1 = sin(vec.y/2);
		float s2 = sin(vec.z/2);
		//calculate each dimesion of quaternion
		x = s0 * c1 * c2 - c0 * s1 * s2;
		y = c0 * s1 * c2 + s0 * c1 * s2;
		z = c0 * c1 * s2 - s0 * s1 * c2;
		w = c0 * c1 * c2 + s0 * s1 * s2;
	}
	//print out value, used for debugging
	void print(){
		printf("<%.4f, %.4f, %.4f> w = %.4f\n", x, y, z, w);
	}
	//Create a rotation matrix from quaternion values
	RotationMatrix rotationMatrix(){
		RotationMatrix r;
		//assign each value of matrix based on quaternion values
		r.rot[0][0] = 1 - 2*(y*y + z*z);
		r.rot[0][1] = 2 * (x*y - w*z);
		r.rot[0][2] = 2 * (w*y + x*z);

		r.rot[1][0] = 2 * (x*y + w*z);
		r.rot[1][1] = 1 - 2*(x*x + z*z);
		r.rot[1][2] = 2 * (-w*x + y*z);

		r.rot[2][0] = 2 * (-w*y + x*z);
		r.rot[2][1] = 2 * (w*x + y*z);
		r.rot[2][2] = 1 - 2*(x*x  + y*y);
		return r;
	}
};

//Camera structure to store camera infomration
struct  Camera{
	//fov of camera
	const float fov = M_PI_2 / 90.0 * 50.0;
	//positions of camera
	Vector3 position;
	//rotation of camrea
	Quaternion direction;

	//Get screen posotion of point from camera info
	Vector3 screenPos(Vector3 vec){
		Vector3 ret;

		//prevent domain errors
		if(vec.x == 0){
			vec.x == 0.001;
		}

		//calcualte x and y screeen position
		ret.x = (vec.z / vec.x) / tan(fov / 2) / 2;
		ret.y = (vec.y / vec.x) / tan(fov / 2);

		//calculate distance for from camera form z value
		ret.z = sqrt(vec.x*vec.x + vec.y*vec.y + vec.z*vec.z);
		return ret;
	}
};


//constant used for output informaiton
#define lineCount 193
#define screenWidth 120
#define screenHeight 30
#define blockerCount 7

int main(){
	//name and identifying informaiton
	printf ("************************************************\n");
	printf ("*  Name:  Brandon Young    Date:  11/14/21     *\n");
	printf ("*  Seat:  20    File:  APP_C31_1.cpp           *\n");
	printf ("*  Instructor:  PAC 08:00                      *\n");
	printf("************************************************\n\n");

	//define varaible for timing
	int START_TIME, TOTAL_RUNTIME, GREEN_TIME, YELLOW_TIME, LOOP_TIME;

	//Get total runtime
	printf("Total Program Runtime (seconds): ");
	scanf("%i", &TOTAL_RUNTIME);

	//intput green time seconds
	printf("Green light time (seconds): ");
	scanf("%i", &GREEN_TIME);

	//inptu time for yellow light
	printf("yellow light time (seconds): ");
	scanf("%i", &YELLOW_TIME);

	//initilize time variable
	START_TIME = time(NULL);
	LOOP_TIME = time(NULL);

	//create camera variable
	Camera camera;

	//set camera starting position
	camera.position = (Vector3) {.x=-2,.y=1.3, .z=-4.5};

	//set camera rotation coutn variable
	float z = 0.6;

	//set position of stop light based on time
	float disStop = 4  + GREEN_TIME * 1.85;

	//Define position of lines in 3d space
	Vector3 lines[lineCount][2] = {
		//Road lines
		{{.x=-6, .y=0, .z=0}, {.x=100, .y=0, .z=0}},
		{{.x=-6, .y=0, .z=-3.5}, {.x=100, .y=0, .z=-3.5}},
		{{.x=-6, .y=0, .z=3.5}, {.x=100, .y=0, .z=3.5}},

		//Stop light stop	
		{{.x=disStop, .y=2, .z=1.5}, {.x=disStop, .y=3.5, .z=1.5}},
		{{.x=disStop, .y=2, .z=2.0}, {.x=disStop, .y=3.5, .z=2.0}},

		{{.x=disStop, .y=2, .z=1.5}, {.x=disStop, .y=2, .z=2.0}},
		{{.x=disStop, .y=2.5, .z=1.5}, {.x=disStop, .y=2.5, .z=2.0}},
		{{.x=disStop, .y=3.0, .z=1.5}, {.x=disStop, .y=3.0, .z=2.0}},
		{{.x=disStop, .y=3.5, .z=1.5}, {.x=disStop, .y=3.5, .z=2.0}},

		//stop light symbol
		{{.x=disStop, .y=2.25, .z=1.75}, {.x=disStop, .y=2.35, .z=1.75}},

		//unused extra stop light
		// {{.x=0, .y=2, .z=1.5}, {.x=0, .y=3.5, .z=1.5}},
		// {{.x=0, .y=2, .z=2.0}, {.x=0, .y=3.5, .z=2.0}},

		// {{.x=0, .y=2, .z=1.5}, {.x=0, .y=2, .z=2.0}},
		// {{.x=0, .y=2.5, .z=1.5}, {.x=0, .y=2.5, .z=2.0}},
		// {{.x=0, .y=3.0, .z=1.5}, {.x=0, .y=3.0, .z=2.0}},
		// {{.x=0, .y=3.5, .z=1.5}, {.x=0, .y=3.5, .z=2.0}},
		// {{.x=0, .y=2.25, .z=1.75}, {.x=0, .y=2.35, .z=1.75}},
	};

	//Ascii letter to use while drawing L is special line
	char letters[lineCount] = {
		//Road lines
		'L',
		'#',
		'#',

		//Stop light style
		'&',
		'&',
		'&',
		'&',
		'&',
		'&',
		'G',

		//Unused stop light sytle
		'&',
		'&',
		'&',
		'&',
		'&',
		'&',
		'G',

	};

	//create blocker to block thing behind other things
	Vector3 blocker[blockerCount][2] = {
		{{.x=7.1, .y=0, .z=6}, {.x=7.1, .y=0, .z=12}},
	};

	//Start house index
	int linesIndex = 17;
	int blockerIndex = 0;

	//start house positions
	float xStartValue = 2;
	for(int i = 0; i < 6; i++){
		//creat first window
		lines[linesIndex+0][0] = (Vector3) {.x=xStartValue+1, .y=1, .z=6.0};
		lines[linesIndex+0][1] = (Vector3) {.x=xStartValue+2, .y=1, .z=6.0};
		lines[linesIndex+1][0] = (Vector3) {.x=xStartValue+1, .y=2, .z=6.0};
		lines[linesIndex+1][1] = (Vector3) {.x=xStartValue+2, .y=2, .z=6.0};
		lines[linesIndex+2][0] = (Vector3) {.x=xStartValue+1, .y=1, .z=6.0};
		lines[linesIndex+2][1] = (Vector3) {.x=xStartValue+1, .y=2, .z=6.0};
		lines[linesIndex+3][0] = (Vector3) {.x=xStartValue+2, .y=1, .z=6.0}; 
		lines[linesIndex+3][1] = (Vector3) {.x=xStartValue+2, .y=2, .z=6.0};

		//creat second window
		lines[linesIndex+4][0] = (Vector3) {.x=xStartValue+3, .y=1, .z=6.0};
		lines[linesIndex+4][1] = (Vector3) {.x=xStartValue+4, .y=1, .z=6.0};
		lines[linesIndex+5][0] = (Vector3) {.x=xStartValue+3, .y=2, .z=6.0};
		lines[linesIndex+5][1] = (Vector3) {.x=xStartValue+4, .y=2, .z=6.0};
		lines[linesIndex+6][0] = (Vector3) {.x=xStartValue+3, .y=1, .z=6.0};
		lines[linesIndex+6][1] = (Vector3) {.x=xStartValue+3, .y=2, .z=6.0};
		lines[linesIndex+7][0] = (Vector3) {.x=xStartValue+4, .y=1, .z=6.0};
		lines[linesIndex+7][1] = (Vector3) {.x=xStartValue+4, .y=2, .z=6.0};

		//create thrid window
		lines[linesIndex+8][0] = (Vector3) {.x=xStartValue+1, .y=5, .z=6.0};
		lines[linesIndex+8][1] = (Vector3) {.x=xStartValue+2, .y=5, .z=6.0};
		lines[linesIndex+9][0] = (Vector3) {.x=xStartValue+1, .y=7, .z=6.0};
		lines[linesIndex+9][1] = (Vector3) {.x=xStartValue+2, .y=7, .z=6.0};
		lines[linesIndex+10][0] = (Vector3) {.x=xStartValue+1, .y=5, .z=6.0};
		lines[linesIndex+10][1] = (Vector3) {.x=xStartValue+1, .y=7, .z=6.0};
		lines[linesIndex+11][0] = (Vector3) {.x=xStartValue+2, .y=5, .z=6.0};
		lines[linesIndex+11][1] = (Vector3) {.x=xStartValue+2, .y=7, .z=6.0};

		//create fourth window
		lines[linesIndex+12][0] = (Vector3) {.x=xStartValue+3, .y=5, .z=6.0};
		lines[linesIndex+12][1] = (Vector3) {.x=xStartValue+4, .y=5, .z=6.0};
		lines[linesIndex+13][0] = (Vector3) {.x=xStartValue+3, .y=7, .z=6.0};
		lines[linesIndex+13][1] = (Vector3) {.x=xStartValue+4, .y=7, .z=6.0};
		lines[linesIndex+14][0] = (Vector3) {.x=xStartValue+3, .y=5, .z=6.0};
		lines[linesIndex+14][1] = (Vector3) {.x=xStartValue+3, .y=7, .z=6.0};
		lines[linesIndex+15][0] = (Vector3) {.x=xStartValue+4, .y=5, .z=6.0};
		lines[linesIndex+15][1] = (Vector3) {.x=xStartValue+4, .y=7, .z=6.0};

		//create depth lines
		lines[linesIndex+16][0] = (Vector3) {.x=xStartValue+0, .y=0, .z=6.0};
		lines[linesIndex+16][1] = (Vector3) {.x=xStartValue+0, .y=0, .z=11.0};
		lines[linesIndex+17][0] = (Vector3) {.x=xStartValue+0, .y=8, .z=6.0};
		lines[linesIndex+17][1] = (Vector3) {.x=xStartValue+0, .y=8, .z=11.0};

		//create vertical depth line
		lines[linesIndex+18][0] = (Vector3) {.x=xStartValue+0, .y=0, .z=11.0};
		lines[linesIndex+18][1] = (Vector3) {.x=xStartValue+0, .y=8, .z=11.0};

		//creat front of house box
		lines[linesIndex+19][0] = (Vector3) {.x=xStartValue+0, .y=0, .z=6.0};
		lines[linesIndex+19][1] = (Vector3) {.x=xStartValue+0, .y=8, .z=6.0};
		lines[linesIndex+20][0] = (Vector3) {.x=xStartValue+5, .y=0, .z=6.0};
		lines[linesIndex+20][1] = (Vector3) {.x=xStartValue+5, .y=8, .z=6.0};
		lines[linesIndex+21][0] = (Vector3) {.x=xStartValue+0, .y=0, .z=6.0};
		lines[linesIndex+21][1] = (Vector3) {.x=xStartValue+5, .y=0, .z=6.0};
		lines[linesIndex+22][0] = (Vector3) {.x=xStartValue+0, .y=8, .z=6.0};
		lines[linesIndex+22][1] = (Vector3) {.x=xStartValue+5, .y=8, .z=6.0};

		//creat house blocker to block out overlapping housees
		blocker[blockerIndex][0] = (Vector3) {.x=xStartValue+5.1, .y=0, .z=6};
		blocker[blockerIndex][1] = (Vector3) {.x=xStartValue+5.1, .y=0, .z=12};

		//assigne house style
		for(int k = 0; k < 23; k++){
			letters[linesIndex+k] = 'L';
		}
		//incremetn position counter
		linesIndex += 23;
		blockerIndex++;
		xStartValue += 10;
	}

	//Car styling
	int carSize = 38;
	for(int i = lineCount - carSize; i < lineCount; i++){
		letters[i] = 'L';
	}

	
	//left side conneciton of car
	lines[linesIndex+0][0] = (Vector3) {.x=1.5, .y=0.8, .z=2.5};
	lines[linesIndex+0][1] = (Vector3) {.x=4, .y=0.8, .z=2.5};
	linesIndex += 1;

	//Top Side empties car preventing overlap
	lines[linesIndex+0][0] = (Vector3) {.x=1.5, .y=0.84, .z=1.3};
	lines[linesIndex+0][1] = (Vector3) {.x=3.5, .y=0.84, .z=1.3};
	lines[linesIndex+1][0] = (Vector3) {.x=1.5, .y=0.95, .z=1.3};
	lines[linesIndex+1][1] = (Vector3) {.x=3.5, .y=0.95, .z=1.3};
	lines[linesIndex+2][0] = (Vector3) {.x=1.5, .y=1.0, .z=1.3};
	lines[linesIndex+2][1] = (Vector3) {.x=3.5, .y=1.0, .z=1.3};
	//set style for overlatp
	for(int i = linesIndex; i < linesIndex+3; i++){
		letters[i] = ' ';
	}
	linesIndex += 3;

	//Wheel 1
	lines[linesIndex+0][0] = (Vector3) {.x=1.3, .y=0.0, .z=1};
	lines[linesIndex+0][1] = (Vector3) {.x=1.6, .y=0.0, .z=1};
	lines[linesIndex+1][0] = (Vector3) {.x=1.1, .y=0.2, .z=1};
	lines[linesIndex+1][1] = (Vector3) {.x=1.8, .y=0.2, .z=1};
	lines[linesIndex+2][0] = (Vector3) {.x=1.3, .y=0.0, .z=1.08};
	lines[linesIndex+2][1] = (Vector3) {.x=1.1, .y=0.4, .z=1.08};

	//wheel 2
	lines[linesIndex+3][0] = (Vector3) {.x=3.4, .y=0.0, .z=1};
	lines[linesIndex+3][1] = (Vector3) {.x=3.7, .y=0.0, .z=1};
	lines[linesIndex+4][0] = (Vector3) {.x=3.2, .y=0.2, .z=1};
	lines[linesIndex+4][1] = (Vector3) {.x=3.9, .y=0.2, .z=1};
	lines[linesIndex+5][0] = (Vector3) {.x=3.4, .y=0.0, .z=1.08};
	lines[linesIndex+5][1] = (Vector3) {.x=3.2, .y=0.4, .z=1.08};

	//wheel 3
	lines[linesIndex+6][0] = (Vector3) {.x=1.1, .y=0.4, .z=2.5};
	lines[linesIndex+6][1] = (Vector3) {.x=1.2, .y=0.0, .z=2.5};
	lines[linesIndex+7][0] = (Vector3) {.x=1.1, .y=0.4, .z=2.42};
	lines[linesIndex+7][1] = (Vector3) {.x=1.2, .y=0.0, .z=2.42};
	//set wheel style
	for(int i = linesIndex; i < linesIndex+8; i++){
		letters[i] = '8';
	}
	linesIndex += 8;

	//prevent overllapping of sides
	lines[linesIndex+0][0] = (Vector3) {.x=1, .y=0.5, .z=1};
	lines[linesIndex+0][1] = (Vector3) {.x=4, .y=0.5, .z=1};
	lines[linesIndex+1][0] = (Vector3) {.x=1, .y=0.6, .z=1};
	lines[linesIndex+1][1] = (Vector3) {.x=4, .y=0.6, .z=1};
	lines[linesIndex+2][0] = (Vector3) {.x=1, .y=0.7, .z=1};
	lines[linesIndex+2][1] = (Vector3) {.x=4, .y=0.7, .z=1};
	//set style of to prevent overlap
	for(int i = linesIndex; i < linesIndex+3; i++){
		letters[i] = ' ';
	}
	linesIndex += 3;

	//side of car box
	lines[linesIndex+0][0] = (Vector3) {.x=4, .y=0.4, .z=1};
	lines[linesIndex+0][1] = (Vector3) {.x=4, .y=0.8, .z=1};
	lines[linesIndex+1][0] = (Vector3) {.x=1, .y=0.4, .z=1};
	lines[linesIndex+1][1] = (Vector3) {.x=4, .y=0.4, .z=1};
	linesIndex += 2;

	//prevent overlap iside of car
	lines[linesIndex+0][0] = (Vector3) {.x=1, .y=0.5, .z=1};
	lines[linesIndex+0][1] = (Vector3) {.x=1, .y=0.5, .z=2.5};
	lines[linesIndex+1][0] = (Vector3) {.x=1, .y=0.6, .z=1};
	lines[linesIndex+1][1] = (Vector3) {.x=1, .y=0.6, .z=2.5};
	lines[linesIndex+2][0] = (Vector3) {.x=1, .y=0.65, .z=1};
	lines[linesIndex+2][1] = (Vector3) {.x=1, .y=0.65, .z=2.5};
	lines[linesIndex+3][0] = (Vector3) {.x=1, .y=0.7, .z=1};
	lines[linesIndex+3][1] = (Vector3) {.x=1, .y=0.7, .z=2.5};
	lines[linesIndex+4][0] = (Vector3) {.x=1, .y=0.8, .z=1.1};
	lines[linesIndex+4][1] = (Vector3) {.x=4, .y=0.8, .z=1.1};
	//set style of prevent overlap
	for(int i = linesIndex; i < linesIndex+5; i++){
		letters[i] = ' ';
	}
	linesIndex += 5;


	//Back horizontals of car
	lines[linesIndex+0][0] = (Vector3) {.x=1, .y=0.4, .z=1};
	lines[linesIndex+0][1] = (Vector3) {.x=1, .y=0.4, .z=2.5};
	lines[linesIndex+1][0] = (Vector3) {.x=1, .y=0.8, .z=1};
	lines[linesIndex+1][1] = (Vector3) {.x=1, .y=0.8, .z=2.5};

	//back verticals fo car
	lines[linesIndex+2][0] = (Vector3) {.x=1, .y=0.4, .z=1};
	lines[linesIndex+2][1] = (Vector3) {.x=1, .y=0.8, .z=1};
	lines[linesIndex+3][0] = (Vector3) {.x=1, .y=0.4, .z=2.5};
	lines[linesIndex+3][1] = (Vector3) {.x=1, .y=0.8, .z=2.5};
	linesIndex += 4;

	//Connection Front and back on car
	lines[linesIndex+0][0] = (Vector3) {.x=1, .y=0.8, .z=1};
	lines[linesIndex+0][1] = (Vector3) {.x=4, .y=0.8, .z=1};
	linesIndex += 1;
	lines[linesIndex+0][0] = (Vector3) {.x=1, .y=0.8, .z=2.5};
	lines[linesIndex+0][1] = (Vector3) {.x=1.5, .y=0.8, .z=2.5};
	linesIndex += 1;

	//Top Front of car
	lines[linesIndex+0][0] = (Vector3) {.x=3.1, .y=1.1, .z=1.3};
	lines[linesIndex+0][1] = (Vector3) {.x=3.1, .y=1.1, .z=2.2};
	letters[linesIndex+0] = '-';
	lines[linesIndex+1][0] = (Vector3) {.x=3.5, .y=0.8, .z=1.14};
	lines[linesIndex+1][1] = (Vector3) {.x=3.1, .y=1.1, .z=1.3};
	linesIndex += 2;

	//prevent overlap on top area of car
	lines[linesIndex+0][0] = (Vector3) {.x=1.6, .y=0.84, .z=1.2};
	lines[linesIndex+0][1] = (Vector3) {.x=1.6, .y=0.84, .z=2.3};
	lines[linesIndex+1][0] = (Vector3) {.x=1.6, .y=0.93, .z=1.2};
	lines[linesIndex+1][1] = (Vector3) {.x=1.6, .y=0.93, .z=2.3};
	lines[linesIndex+2][0] = (Vector3) {.x=1.6, .y=1.0, .z=1.2};
	lines[linesIndex+2][1] = (Vector3) {.x=1.6, .y=1.0, .z=2.3};
	//set prevent overlap style
	for(int i = linesIndex; i < linesIndex+3; i++){
		letters[i] = ' ';
	}
	linesIndex += 3;

	//Top Connections of car
	lines[linesIndex+0][0] = (Vector3) {.x=1.9, .y=1.1, .z=1.3};
	lines[linesIndex+0][1] = (Vector3) {.x=3.1, .y=1.1, .z=1.3};
	lines[linesIndex+1][0] = (Vector3) {.x=1.9, .y=1.1, .z=2.2};
	lines[linesIndex+1][1] = (Vector3) {.x=3.1, .y=1.1, .z=2.2};
	linesIndex += 2;

	//Top fo car
	lines[linesIndex+0][0] = (Vector3) {.x=1.9, .y=1.1, .z=1.3};
	lines[linesIndex+0][1] = (Vector3) {.x=1.9, .y=1.1, .z=2.2};
	lines[linesIndex+1][0] = (Vector3) {.x=1.5, .y=0.8, .z=1.14};
	lines[linesIndex+1][1] = (Vector3) {.x=1.9, .y=1.1, .z=1.3};
	lines[linesIndex+2][0] = (Vector3) {.x=1.5, .y=0.8, .z=2.36};
	lines[linesIndex+2][1] = (Vector3) {.x=1.9, .y=1.1, .z=2.2};
	linesIndex += 3;

	//main loop end when timer runs out
	while(time(NULL) - START_TIME < TOTAL_RUNTIME){

		//rotate camre beggingin mvoemetns
		if(z > 0){
			z -= 0.002;
			camera.direction.fromVector3((Vector3) {.x=0.0,.y=z, .z=0.0});
		}

		//move car if green
		if(time(NULL) - LOOP_TIME < GREEN_TIME){
			//set move amount
			float moveX = 0.02;

			//move camera
			camera.position.x += moveX;

			//move camera on z axis for opening movemetns
			if(camera.position.z < 1.75){
				camera.position.z += 0.02;
			}

			//move each line of car
			for(int i = lineCount - carSize; i < lineCount; i++){
				lines[i][0].x += moveX;
				lines[i][1].x += moveX;
			}
		//Change light if yellow
		}else if(time(NULL) - LOOP_TIME < GREEN_TIME + YELLOW_TIME){
			//change position of light
			lines[9][0] = (Vector3) {.x=disStop, .y=2.75, .z=1.75};
			lines[9][1] = (Vector3) {.x=disStop, .y=2.85, .z=1.75};
			//chagne style of light
			letters[9] = 'Y';
		//chagne light to red
		}else{
			//change position of light
			lines[9][0] = (Vector3) {.x=disStop, .y=3.25, .z=1.75};
			lines[9][1] = (Vector3) {.x=disStop, .y=3.35, .z=1.75};\
			//chang style of light
			letters[9] = 'R';
		}

		//reset sequene if complete
		if(time(NULL) - LOOP_TIME > 2*(GREEN_TIME + YELLOW_TIME)){
			//find initial position of car
			float pos = lines[lineCount - 1][0].x - 1.9;
			//set camera to initial position
			camera.position.x -= pos;
			//move car to initial position
			for(int i = lineCount - carSize; i < lineCount; i++){
				lines[i][0].x -= pos;
				lines[i][1].x -= pos;
			}
			//reset loop timer
			LOOP_TIME = time(NULL);
			//reset stoplight position
			lines[9][0] = {.x=disStop, .y=2.25, .z=1.75};
			lines[9][1] =  {.x=disStop, .y=2.35, .z=1.75};
			//reset stop light style
			letters[9] = 'G';
		}

		//create rotation matrix for mapping
		RotationMatrix r = camera.direction.rotationMatrix();

		//initilize arrays to keep track of screen
		char screenPrint[screenHeight][screenWidth + 1];
		float screenBlockers[screenHeight][screenWidth];

		//start array with render distance of 100 and empty values
		for(int y = 0; y < screenHeight; y++){
			for(int x = 0; x < screenWidth; x++){
				screenPrint[y][x] = ' ';
				screenBlockers[y][x] = 100.0;
			}
			//add end of string char
			screenPrint[y][screenWidth] = '\0';
		}

		//loop trhough all blockers and set render dis of those points
		for(int k = 0; k < blockerCount;k++){
			//find blocker retatlive to camera
			Vector3 a = r.applyTo(blocker[k][0] - camera.position);
			Vector3 b = r.applyTo(blocker[k][1] - camera.position);

			//ignore if behind camera
			if(a.x <= 0.3 || b.x <= 0.3) continue;

			//find screen position
			a = camera.screenPos(a);
			b = camera.screenPos(b);

			//find pixel position
			float sX = ((a.x * (screenWidth / 2.0)) + (screenWidth / 2.0)); 
			float eX = ((b.x * (screenWidth / 2.0)) + (screenWidth / 2.0)); 

			//find total distance between start and end pixels
			float deltaX = eX - sX;
			
			//loop trhough pixels and set render distance for each one
			for(int x = round(sX); fabs(x - sX) < fabs(deltaX); x+=(deltaX / fabs(deltaX))){
				//check if in screen size
				if(x >= 0 && x < screenWidth){
					for(int y = 0; y < screenHeight; y++){
						//reduce render distance if needed
						if(screenBlockers[y][x] > a.z){
							screenBlockers[y][x] = a.z;
						}
					}
				}
			}
		}

		//loop through all lines and draw them
		for(int k = 0; k < lineCount; k++){
			//find relative positions
			Vector3 start = lines[k][0] - camera.position;
			Vector3 end = lines[k][1] - camera.position;

			//rotate relative positions based on camerea
			start = r.applyTo(start);
			end = r.applyTo(end);

			//ignroe if behind camera
			if(start.x <= 0.1 && end.x <= 0.1){
				continue;
			}
			//fix start values if behind camrea
			if(start.x <= 0.1){
				//set one behind camera to infornt of camera
				float x = 0.3;
				float deltaX = end.x - start.x;
				if(deltaX < 0.1) continue;
				float perc = fabs((x-start.x) / deltaX);
				//adjust each value to keep line constant
				start.y = (end.y - start.y) * perc + start.y;
				start.z = (end.z - start.z) * perc + start.z;
				start.x = x;
			}

			//fix end values if behind camera
			if(end.x <= 0.1){
				//set to infornt of camera
				float x = 0.3;
				float deltaX = start.x - end.x;
				if(deltaX < 0.1) continue;
				float perc = fabs((x-end.x) / deltaX);
				//adjust each value to keep line cosntant
				end.y = (start.y - end.y) * perc + end.y;
				end.z = (start.z - end.z) * perc + end.z;
				end.x = x;
			}

			//find line start and end pos on screen
			start = camera.screenPos(start);
			end = camera.screenPos(end);

			//adjust to pixel values
			float sX = ((start.x * (screenWidth / 2.0)) + (screenWidth / 2.0)); 
			float sY = ((start.y * (screenHeight / 2.0)) + (screenHeight / 2.0));
			float eX = ((end.x * (screenWidth / 2.0)) + (screenWidth / 2.0)); 
			float eY = ((end.y * (screenHeight / 2.0)) + (screenHeight / 2.0));

			//find delta valuse
			float deltaX = eX - sX;
			float deltaY = eY - sY;

			//check if vertical or horizontal lines
			if(fabs(deltaX) > fabs(deltaY) * 1.4){
				//loop through horizontal lines
				for(int i = round(sX); fabs(i - sX) <= fabs(deltaX); i+= (deltaX / fabs(deltaX))){
					//find y point based on x point
					float perc = (fabs(i - sX)) / fabs(deltaX);
					float yVal = perc*deltaY + sY;
					int yV = round(yVal);
					float symbol = yVal - yV;
					//check if line is on screen
					if(yV >= 0 && yV < screenHeight && i >= 0 && i < screenWidth){
						//check if line is covered by blocker
						if(screenBlockers[yV][i] < start.z) continue;
						//do special style
						if(letters[k] == 'L'){
							screenPrint[yV][i] = (fabs(symbol) < 0.166) ? '-' : (symbol > 0) ? '\'' : '.';
						//do non special style
						}else screenPrint[yV][i] = letters[k];
					}
				}
			//vertical lines
			}else{
				//creat previsou pos for special lines
				int ii = round(sY) - (deltaY / fabs(deltaY));
				float percII = -((fabs(ii - sY)) / fabs(deltaY));
				float prevX = percII * deltaX + sX;
				int prevXV = round(prevX);
				//loop through line vertically
				for(int i = round(sY); fabs(i - sY) <= fabs(deltaY); i+= (deltaY / fabs(deltaY))){
					//find x position based on y position
					float perc = (fabs(i - sY)) / fabs(deltaY);
					float xVal = perc*deltaX + sX;
					int xV = round(xVal);

					//find next x position for special lines
					float nextI = i + (deltaY / fabs(deltaY));
					float nextPerc = (fabs(nextI - sY)) / fabs(deltaY);
					float nextXVal = nextPerc * deltaX + sX;
					int nextXV = round(nextXVal);
					//check if lines is on screen
					if(xV >= 0 && xV < screenWidth && i >= 0 && i < screenHeight){
						//ignore if covered by blocker
						if(screenBlockers[i][xV] < start.z) continue;
						//check sytle
						if(letters[k] == 'L'){
							//draw special style based on direction of line
							screenPrint[i][xV] = '|';
							if((deltaY) / fabs(deltaX) < 0){
								if(nextXV > xV && prevXV < xV) screenPrint[i][xV] = '\\';
								else if(nextXV < xV && prevXV > xV) screenPrint[i][xV] = '/';
								else screenPrint[i][xV] = '|';
							}else{
								if(nextXV > xV && prevXV < xV) screenPrint[i][xV] = '/';
								else if(nextXV < xV && prevXV > xV) screenPrint[i][xV] = '\\';
								else screenPrint[i][xV] = '|';
							}
							prevXV = xV;
						//draw default style
						}else screenPrint[i][xV] = letters[k];
					}
				}
			}
		}

		//creat array to adjust 2d array to 1d
		char a[(screenWidth + 1) * screenHeight + 1];
		//copy screen 2d array into new 1d array
		for(int i = 0; i < screenHeight; i++){
			//copy line
			strcpy(a+((screenWidth + 1) * i * sizeof(char)), screenPrint[screenHeight - i - 1]);
			//add endline char
			strcpy(a+((screenWidth + 1) * (i + 1) * sizeof(char)) - 1, "\n");
			//printf("%s\n", screenPrint[i]);
		}
		//add end str char
		strcpy(a + ((screenWidth + 1) * screenHeight * sizeof(char)), "\0");

		//print blank space before line
		printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
		//print out value for N/s and E/W based on time
		//green light n/s
		if(time(NULL) - LOOP_TIME < GREEN_TIME){
			printf("N/S GREEN - E/W RED\n");
		//yellow light n/s
		}else if(time(NULL) - LOOP_TIME < GREEN_TIME + YELLOW_TIME){
			printf("N/S YELLOW - E/W RED\n");
		//green light e/w
		}else if(time(NULL) - LOOP_TIME < 2 * GREEN_TIME + YELLOW_TIME){
			printf("N/S RED - E/W GREEN\n");
		//yellow light e/w
		}else{
			printf("N/S RED - E/W YELLOW\n");
		}
		//print ascii animation
		printf("%s", a);

		//delay until next frame
		usleep(10000);
	}

	//clear screen once done
	printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\tDrive safe\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
}