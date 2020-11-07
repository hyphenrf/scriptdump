#define LED        LED_BUILTIN
#define MORSE_UNIT 100

/* TODO: storage can be more efficient */


static int const SEP     =   MORSE_UNIT;
static int const DIT     =   MORSE_UNIT;
static int const DAH     = 3*MORSE_UNIT;
static int const END_LTR = 3*MORSE_UNIT;
static int const END_WRD = 7*MORSE_UNIT;

static int code(char const c)
{
  switch (c) {
    // dit = 10, dah = 11, ew = 01
    case ' ': return 0x1;

    case '0': return 0x3ff;
    case '1': return 0x3fe;
    case '2': return 0x3fa;
    case '3': return 0x3ea;
    case '4': return 0x3aa;
    case '5': return 0x2aa;
    case '6': return 0x2ab;
    case '7': return 0x2af;
    case '8': return 0x2bf;
    case '9': return 0x2ff;

    case 'A': case 'a': return 0xe;
    case 'B': case 'b': return 0xab;
    case 'C': case 'c': return 0xbb;
    case 'D': case 'd': return 0x2b;
    case 'E': case 'e': return 0x2;
    case 'F': case 'f': return 0xba;
    case 'G': case 'g': return 0x2f;
    case 'H': case 'h': return 0xaa;
    case 'I': case 'i': return 0xa;
    case 'J': case 'j': return 0xfe;
    case 'K': case 'k': return 0x3b;
    case 'L': case 'l': return 0xae;
    case 'M': case 'm': return 0xf;
    case 'N': case 'n': return 0xb;
    case 'O': case 'o': return 0x3f;
    case 'P': case 'p': return 0xbe;
    case 'Q': case 'q': return 0xef;
    case 'R': case 'r': return 0x2e;
    case 'S': case 's': return 0x2a;
    case 'T': case 't': return 0x3;
    case 'U': case 'u': return 0x3a;
    case 'V': case 'v': return 0xea;
    case 'W': case 'w': return 0x3e;
    case 'X': case 'x': return 0xeb;
    case 'Y': case 'y': return 0xfb;
    case 'Z': case 'z': return 0xef;

    default: return 0x0;
  }
}



/* Impl: */

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  to_morse("Send Nudes");
  delay(15*MORSE_UNIT);
}


/* Funcs: */

void to_morse(char const * message)
{
  while (*message) do_morse(code(*(message++)));
}

void do_morse(int letter)
{
  if (!letter) return; // for the default case in lookup table

  while (letter) {
    switch (letter & 3) {
      case 1:
        do_endword();
        goto endroutine;
      case 2:
        do_bit(DIT);
        break;
      case 3:
        do_bit(DAH);
        break;
    }
    letter >>= 2;
  }
  delay(END_LTR - SEP); // because last letter delays SEP

endroutine:
  return;
}

void do_endword(void)
{
  digitalWrite(LED, LOW);
  delay(END_WRD);
}

void do_bit(int const t)
{
  digitalWrite(LED, HIGH);
  delay(t);
  digitalWrite(LED, LOW);
  delay(SEP);
}
