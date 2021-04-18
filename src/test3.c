int a() {
    b();
    return 5;
}

int b() {
    c();
    return 4;
}

int c() {
    d();
    return 3;
}

int d() {
    e();
    return 2;
}

int e() {
    return 1;
}

int main() {
    a();
    return 0;
}