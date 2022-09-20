class Term
{
 public:
 // default constructor
 Term();
 // initialize with the given query string and weight
 Term(string query, long weight);
 // compare two terms in descending order by weight
 // if t1 and t2 are in descending order by weight, return 1
 // if they are of the same weight, return 0;
 // otherwise, return -1
 static int compareByWeight(Term t1, Term t2);
 // compares two terms in lexicographic order but using only
 // the first r characters of each query
 // if the first r characters of t1 and t2 are in lexicographic order, return 1
 // if they are of the same r characters, return 0;
 // otherwise, return -1
 static int compareByPrefix(Term t1, Term t2, int r);
 // define the operator “<” for Term class (as friend function)
friend bool operator<(Term t1, Term t2);
 // define the operator “<<” for Term class (as friend function)
 // so that it can send the Term object directly to cout, in the following format:
 // the weight followed by a tab key, then followed by the query
friend ostream& operator<<(ostream& out, const Term& t);
 // assign “friendship” to the class named Autocomplete
 // so that Autocomplete class can directly access the private data members
 // of Term class. Not the other way around.
friend class Autocomplete;
 private:
 string query;
 long weight;
};