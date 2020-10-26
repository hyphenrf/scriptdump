/* A small program to demonstrate:
 *
 * coercion with unions
 * process calling
 * turning structs into buffers with [struct] syntax
 * D strings internal repr 
 * and scope finalizers */

import std.process;
import std.stdio;
import std.file;

union U1 {
	int a;
	string b;
}

union U2 {
	struct {size_t l; size_t p;}; // a deconstruction of the D string
	string b;
}

struct d_string { // D strings internal repr. Equivalent of the above deconstruction
	size_t length;
	char * cstring;
}

void main()
{
	U1 x;
	U2 y;
	auto o = File("unions.out", "wb");
	scope(exit) o.close();

	string left = "Hello";
	d_string right = {5, cast(char*)"Hello"};

	x.a = 5; // will be erased by below string's length
	x.b = "Hello World";

	y.l = 5; // will be erased ...
	y.b = "Hello World";
	// now y.l and y.p are hello world's length and charptr respectively

	writeln("x.a\t",      x.a);
	writeln("x.b:\t",     x.b);
	writeln("x.sizeof:\t",x.sizeof);

	writeln("----------------------------");
	
	writeln("y.l\t",  y.l);
	writefln("y.p:\t0x%X", y.p);
	writeln("y.b:\t", y.b);
	write("cstring cast: ");
	puts(cast(char*)y.p);
	writeln("y.sizeof:\t",y.sizeof);

	writeln("----------------------------");

	o.rawWrite([left]);
	o.rawWrite([right]);
	o.flush();
	auto xxd = executeShell("xxd unions.out");
	writeln(xxd.output); // Should prove to be equivalent
}
