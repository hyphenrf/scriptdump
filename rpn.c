#include <stdio.h>
#include <stdlib.h>
#include <string.h>


short s[2<<16], sp;

inline void
push(short a) { s[sp++] = a; }

inline short
peek(void) { return s[sp-1]; }

inline short
pop(void) { return s[--sp]; }

#define EQ(s1, s2) (!strcmp(s1, s2))

int
main(void)
{
	char *line, *token, *endp = NULL;
	size_t len, n;
	while (1) {
		printf("RPN> ");
		getline(&line, &len, stdin);
		token = strtok(line, "\t\r\n ");
		do {
			     if (EQ(token, ".")) { printf("%d\n", pop()); }
			else if (EQ(token, "=")) { printf("%d\n", peek()); }
			else if (EQ(token, "+")) { push((pop() + pop())); }
			else if (EQ(token, "-")) { push((n = pop(), pop() - n)); }
			else if (EQ(token, "*")) { push((pop() * pop())); }
			else if (EQ(token, "/")) { push((n = pop(), pop() / n)); }
			else if (EQ(token, "?")) {
				printf("Stack Pointer: %d\nStack: ", sp);
				for(int i = 0; i < sp; i++)
					printf("%d ", s[i]);
				printf("\n");
			} else {
				n = strtol(token, &endp, 10);
				if (endp && !(*endp))
					push((short) n);
			}
		} while ((token = strtok(NULL, "\t\r\n ")));
	}

	return 0;
}
