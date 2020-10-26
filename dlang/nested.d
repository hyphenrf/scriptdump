import std.stdio;

void main() {
	int x = 69;

	void nested() {
		write("x = ");
		write(x);
		write("\nThis is a nested function definition!"~" With closure!!\n");
	}

	nested();
}
