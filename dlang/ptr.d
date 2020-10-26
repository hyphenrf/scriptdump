/*
 * Struct casting with pointers
 */
import std.stdio;

struct pub_s {
	int a;
	char[128] b;
}

struct priv_s {
	pub_s pub;
	char[128] secret;
}


int main() {
	priv_s priv = {
				pub: { a:9, b:"thousand!" }, 
				secret: "cool secret!"
	};
	pub_s *pub  = &priv.pub;

	writef("it's over %d %s\n", pub.a, pub.b);
	writef("also:\n");
	writef("%s\n", (cast(priv_s*) pub).secret);

	return 0;
}
