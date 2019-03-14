/*
(?) для заданной булевской функции создает самую быструю схему из элементов или,не. (?)
*/
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <stdlib.h>
using namespace std;

#define VAL_BITS 8
struct Value{
	int x;
	Value():x(0){}
	Value(int xx):x(xx){}
	Value(const Value & v):x(v.x){}
	Value & operator=(Value v){	x=v.x;	return *this;	}
	operator bool()const{	return x;	}
};
Value 	operator~	(Value l)			{	l.x=~l.x;	return l;	}
Value 	operator&	(Value l, Value r)	{	return l.x&r.x;	}
Value 	operator|	(Value l, Value r)	{	return l.x|r.x;	}
Value 	operator<<	(Value l, int i)	{	return l.x<<i;	}
Value 	operator>>	(Value l, int i)	{	return l.x>>i;	}
Value & operator&=	(Value & l, Value r){	l.x&=r.x;	return l;	}
Value & operator|=	(Value & l, Value r){	l.x|=r.x;	return l;	}
Value & operator<<=	(Value & l, int i)	{	l.x<<=i;	return l;	}
Value & operator>>=	(Value & l, int i)	{	l.x>>=i;	return l;	}
bool 	operator==	(Value l, Value r)	{	return l.x==r.x;	}
bool 	operator!=	(Value l, Value r)	{	return l.x!=r.x;	}
bool 	operator<	(const Value & l, const Value & r){	return l.x<r.x;	}
// младшие слева
ostream & operator<<(ostream & str, Value val){
	Value v=1;
	for(int i=0; i<VAL_BITS; i++, v<<=1)
		str<<((bool)(val&v) ? '1' : '0');
	return str;
}

/*
0 -> 01010101
1 -> 00110011
2 -> 00001111
3 -> 00000000
*/
Value arg_generate(int n){
	n=1<<n;
	Value v=1, val=0;
	int j=0;
	bool x=false;
	for(int i=0; i<VAL_BITS; i++, v<<=1){
		if(x)
			val|=v;
		j++;
		if(j==n){
			j=0;
			x=!x;
		}
	}
	return val;
}

struct Name{
	const string & s;
	Name(const string & ss):s(ss){}
};
ostream & operator<<(ostream & str, const Name & n){
	return str<<n.s;
}
/*
aaa
baa
caa
aba
bba
cba
aca
...
*/
bool next_name_ind(char * s,int ind){
	if(s[ind]==0)
		return false;
	if(s[ind]=='c'){
		s[ind]='a';
		return next_name_ind(s,ind+1);
	}
	s[ind]++;
	return true;
}
bool next_name(char * s){
	return next_name_ind(s,0);
}



int count_bc(const string & s){
	int c=0;
	for(unsigned int i=0; i<s.size(); i++)
		if(s[i]!='a')
			c++;
	return c;
}

struct Nodes{
	//name: a b c
	//a - не участвует
	//b - участвует, не инвертировано
	//c - участвует, инвертировано
	vector<pair<string,Value>> arr;
	map<Value,int> fast_vals;
	bool add(const string & name, Value val, int max_ind){
		//поиск и добавление и сохранение уникальности за пределами max_ind
		auto fast_it = fast_vals.find(val);
		if(fast_it==fast_vals.end()){//безусловное добавление
			fast_vals.insert(make_pair(val,arr.size()));
			arr.push_back(make_pair(name,val));
			int i=arr.size()-1;
			cout<<i<<")["<<arr[i].second<<"]"<<arr[i].first<<endl;
			return true;
		}
		else if(fast_it->second>=max_ind){//сохранение уникальности и минимизация
			return false;
			int old_c=count_bc(arr[fast_it->second].first), new_c=count_bc(name);
			if(new_c<old_c){
				arr[fast_it->second].first=name;
				return false;
			}
			if(new_c>old_c)
				return false;
			//new_c==old_c
			cout << "note: (" <<fast_it->second <<") "
				<<Name(arr[fast_it->second].first) <<" == " <<Name(name)<<endl;
			return false;
		}
		return false;//это значение получается за меньшее число шагов
	}
	Value calc(const string & name){
		Value val;
		for(unsigned int i=0; i< name.size(); i++)
			switch(name[i]){
				case 'a': break;
				case 'b': val|= arr[i].second; break;
				case 'c': val|= ~arr[i].second; break;
				default: cerr<<"undefined letter"<<endl; exit(1);
			}
		return val;
	}
	int size()const	{
		return arr.size();
	}
} nodes;
ostream & operator<<(ostream & str, const Nodes & nodes){
	for(int i=0; i<nodes.size(); i++){
		str<<i<<")["<<nodes.arr[i].second<<"]"<<nodes.arr[i].first<<endl;
	}
	return str;
}

int main(){
	int arg_count=3;
	int max_depth=6;
	bool need_search = false;
	Value val_search;
	

	//заполнение аргументных значений
	for(int i=0; i<arg_count; i++){
		Value val = arg_generate(i);
		nodes.add("",val,0);
		if(need_search && val_search==val){
			cout<<nodes;
			exit(0);
		}
	}
	
	int max_ind=0;
	//цикл по глубине
	for(int depth=1; depth<max_depth; depth++){
		cout<<depth<<endl<<nodes;
		int new_size = nodes.size();
		char name[new_size+1];
		for(int i=0; i<new_size; i++)
			name[i]='a';
		name[new_size]=0;
		name[max_ind]='b';
		max_ind=new_size;

		bool flag = false;
		//цикл по всему что возможно на данной глубине
		do{
			Value val = nodes.calc(name);
			if(nodes.add(name,val,max_ind)){
				if(need_search && val_search==val){
					cout<<nodes;
					exit(0);
				}
				flag = true;
			}
		}while(next_name(name));
		//за данной глубине ни чего не удалось добавить
		if(!flag || nodes.size()==1<<(1<<arg_count)){
			cout<<"все аргументы перебраны за "<<depth<<" шагов "<<endl;
			break;
		}
	}
	cout<<nodes;
	exit(0);
}