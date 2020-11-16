import std.stdio: printf;

static nothrow double PI() @nogc @system {
	double pi;
	asm nothrow @nogc @system {
		fldpi;
		fst pi;
	}
	return pi;
}

void main() @nogc {
	double area, pi = PI(), r = 3.0;
	area = r * r * pi;
	printf("Area of a circle r = 3: %.12g\n", area);
}
