/*
перебор всех возможных графов, состоящих не более чем из VERTEX вершин.
*/
#include <map>
#include <iostream>
using std::cout;
using std::endl;

#define VERTEX 4

class GraphVirt;
class GraphMatrix;
void makeDirect(const GraphMatrix & GM, GraphVirt * pGV);
void makeInverse(const GraphMatrix & GM, GraphVirt * pGV);
class GraphMatrix {
	friend void makeDirect(const GraphMatrix & GM, GraphVirt * pGV);
	friend void makeInverse(const GraphMatrix & GM, GraphVirt * pGV);
	bool matrix[VERTEX][VERTEX];
public:
	int stVect[VERTEX]; // вектор степеней
	GraphMatrix() {
		for(int i=0; i<VERTEX; i++)
			for(int j=0; j<VERTEX; j++)
				matrix[i][j]=false;
		for(int i=0; i<VERTEX; i++)
			stVect[i]=0;
	}
	bool next() {
		bool overflow = true;
		for(int i=1; i<VERTEX && overflow; i++) {
			for(int j=0; j<i && overflow; j++) {
				if(matrix[i][j]) {
					matrix[i][j] = false;
					overflow = true;
				}
				else {
					matrix[i][j] = true;
					overflow = false;
				}
			}
		}
			
		for(int i=0; i<VERTEX; i++) {
			int c=0;
			for(int j=0; j<i; j++)
				if(matrix[i][j])
					c++;
			for(int k=i+1; k<VERTEX; k++)
				if(matrix[k][i])
					c++;
			stVect[i]=c;
		}
		return !overflow;
	}
};

class GraphVirt {
	int matrix[VERTEX][VERTEX+1];
public:
	GraphVirt() {
		for(int i=0; i<VERTEX; i++)
			matrix[i][0] = -1; // массив списков, -1 означает конец
	}
	void addEdge(int a, int b) {
		int j=0;
		for(; matrix[a][j]==-1; j++);
		matrix[a][j] = b;
		matrix[a][j+1] = -1;
		j=0;
		for(; matrix[b][j]==-1; j++);
		matrix[b][j] = a;
		matrix[b][j+1] = -1;
	}
	
};
void makeDirect(const GraphMatrix & GM, GraphVirt * pGV) {
	for(int i=0; i<VERTEX; i++)
		for(int j=0; j<i; j++)
			if(GM.matrix)
				pGV->addEdge(i,j);
}
void makeInverse(const GraphMatrix & GM, GraphVirt * pGV) {
	for(int i=0; i<VERTEX; i++)
		for(int j=0; j<i; j++)
			if(!GM.matrix) // !!! difference only here
				pGV->addEdge(i,j);
}

/*
todo
добавить метод печати в GraphVirt
и проверить работоспособность для 3 вершин, потом 4;
добавить и проверить метод проверки на связность туда же
map
*/

int main() {
	GraphMatrix GM;
	do {
		bool cont=false;
		for(int i=1; i<VERTEX; i++)
			if(GM.stVect[i-1]>GM.stVect[i]) {
				cont = true;
				break;
			}
		if(cont) continue;
		
	}
	while(GM.next());
}