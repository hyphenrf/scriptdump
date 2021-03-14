#include <stdint.h>
#include <caml/mlvalues.h>

uint64_t
rdtsc_start()
{
    uint32_t lo, hi;
    __asm__ __volatile__ (
      "mfence \n"
      "lfence \n"
      "rdtsc  \n"
      : "=a" (lo), "=d" (hi)
      :
      : "%ebx", "%ecx");
    return (uint64_t)hi << 32 | lo;
}

uint64_t
rdtsc_stop()
{
    uint32_t lo, hi;
    __asm__ __volatile__ (
      "rdtscp \n"
      "lfence \n"
      : "=a" (lo), "=d" (hi)
      :
      : "%ebx", "%ecx");
    return (uint64_t)hi << 32 | lo;
}
