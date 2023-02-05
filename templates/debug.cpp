namespace Color {
    enum Code {
        FG_RED = 31,
        FG_GREEN = 32,
        FG_BLUE = 34,
        FG_DEFAULT = 39,
        BG_RED = 41,
        BG_GREEN = 42,
        BG_BLUE = 44,
        BG_DEFAULT = 49
    };

    class Modifier {
        Code code;
    public:
        Modifier(Code pCode) : code(pCode) {}

        friend ostream &
        operator<<(ostream &os, const Modifier &mod) {
            return os << "\033[" << mod.code << "m";
        }
    };
}

string to_string(const string& s) {
    return '"' + s + '"';
}

string to_string(char s) {
    return "'" + string(1, s) + "'";
}

string to_string(const char* s) {
    return to_string((string) s);
}
string to_string(bool b) {
    return (b ? "true" : "false");
}
template <typename A, typename B>
string to_string(pair<A, B> p) {
    return "(" + to_string(p.first) + ", " + to_string(p.second) + ")";
}
template <typename A>
string to_string(A v) {
    bool first = true;
    string res = "{";
    for (const auto &x : v) {
        if (!first) {
            res += ", ";
        }
        first = false;
        res += to_string(x);
    }
    res += "}";
    return res;
}


void debug_out() { cerr << endl; }
template <typename Head, typename... Tail>
void debug_out(Head H, Tail... T) {
  cerr << " " << to_string(H);
  debug_out(T...);
}
#ifdef LOCAL
Color::Modifier red = Color::Modifier(Color::FG_RED);
Color::Modifier def = Color::Modifier(Color::FG_DEFAULT);
#define debug(...) cerr << red << "[" << #__VA_ARGS__ << "]:", debug_out(__VA_ARGS__) << def << endl;
#else
#define debug(...) 42
#endif

