#include <iostream>
#include <string>

using namespace std;

int middlePosition(int maximumValue, int minimumValue){
    if ((maximumValue + minimumValue) % 2 == 1) return (maximumValue+minimumValue)/2 + 1;
    return (maximumValue+minimumValue)/2;
}

int main()
{
    int widthOfBuilding;
    int heightOfBuilding;
    cin >> widthOfBuilding >> heightOfBuilding; cin.ignore();

    int numberOfTurns;
    cin >> numberOfTurns; cin.ignore();

    int actualPositionX;
    int actualPositionY;
    cin >> actualPositionX >> actualPositionY; cin.ignore();

    int minimumBombPositionX = 0;
    int maximumBombPositionX = widthOfBuilding - 1;
    int minimumBombPositionY = 0;
    int maximumBombPositionY = heightOfBuilding - 1;

    while (1) {

        string bombDirection; // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
        cin >> bombDirection; cin.ignore();

        if (bombDirection.find("U") != -1) maximumBombPositionY = actualPositionY - 1;
        if (bombDirection.find("R") != -1) minimumBombPositionX = actualPositionX + 1;
        if (bombDirection.find("D") != -1) minimumBombPositionY = actualPositionY + 1;
        if (bombDirection.find("L") != -1) maximumBombPositionX = actualPositionX - 1;

        actualPositionX = middlePosition(maximumBombPositionX,minimumBombPositionX);
        actualPositionY = middlePosition(maximumBombPositionY,minimumBombPositionY);

        cout << actualPositionX << " " << actualPositionY << endl;
    }
}