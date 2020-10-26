import std.stdio;

struct S {
	int a, b, c, d, e;
}

union U {
	int a, b, c, d, e;
}

void main()
{
	S x;
	U y;
	string z;

	writeln(x.sizeof);
	writeln(y.sizeof);
	writeln(z.sizeof);
	
	/* writeln(cast(int) y); fails, if you want to access the string's stored
 	 * length, you must coerce it in a union. */
}
