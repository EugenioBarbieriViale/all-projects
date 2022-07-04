#include <bits/stdc++.h>
using namespace std;

string goto_end(fstream &f) {
	f.seekg(-2,ios_base::end);
	bool keeplooping = true;
	while(keeplooping) {
		char c;
		f.get(c);

		if((int)f.tellg() <= 1) {
			f.seekg(0);
			keeplooping = false;
		}
		else if(c == '\n')
			keeplooping = false;
		else
			f.seekg(-2,ios_base::cur);
	}
	string lastline;
	getline(f,lastline);
	return lastline;
}

int get_value(string x) {
	int ans=0, count=0;
	for (int i=x.length(); i>0; i--) {
		if (isdigit(x[i])!=0) {
			int d = x[i]-'0';
			ans+=d*pow(10,count);
			count++;
		}
	}
	return ans;
}

int commando_centre(fstream &f) {
	int input, count=0;
	string line;
	while (1) {
		cout << " -------------- " << endl;
		cout << "| 1. EXITS     |" << endl;
		cout << "| 2. ENTRIES   |" << endl;
		cout << "| 3. SHOW FILE |" << endl;
		cout << "| 4. GOODBYE   |" << endl;
		cout << " -------------- " << endl;
		cout << ": ";
		cin >> input;
		int tot = get_value(goto_end(f));
		int new_tot=tot;
		switch (input) {
			case 1:
				int loss;
				cout << "Enter quantity: ";
				cin >> loss;
				new_tot-=loss;
				cout << tot << "€ -> " << new_tot << "€"<< endl;
				f << "Loss: " << to_string(loss) << endl;
				f << "Tot: " << to_string(new_tot) << endl;
				break;
			case 2:
				int gain;
				cout << "Enter quantity: ";
				cin >> gain;
				new_tot+=gain;
				cout << tot << "€ -> " << new_tot << "€"<< endl;
				f << "Gain: " << to_string(gain) << endl;
				f << "Tot: " << to_string(new_tot) << endl;
				break;
			case 3:
				f.seekg(0,ios_base::beg);
				while (f) {
					count++;
					getline(f,line);
					if (count>2)
						cout << line << endl;
				}
				break;
			case 4:
				cout << "Bye" << endl;
				return 0;
		}
	}
	return 0;
}

int main() {
	int test=0;
	string user, pass, line;
	cout << "Enter username: ";
	cin >> user;
	cout << "Enter password: ";
	cin >> user;

	fstream f;
	f.open("cbank.txt", ios::in | ios::out | ios::app);
	for (int i=0; i<3; i++) {
		getline(f,line);
		if (line==pass || line==user) test++;
	}
	if (test==2) {
		cout << "Login sucessfull" << endl;
		commando_centre(f);
	} else {
		cout << "Login failed" << endl;
		return 0;
	}

	f.close();
	return 0;
}
