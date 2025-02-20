#include <stdint.h>

struct DataPadded {
  char a;
  long b;
  int c;
};

#pragma pack(push, 1)
typedef struct DataPacked {
  char a;
  long b;
  int c;
} data_t;
#pragma pack(pop)

int main() {
  long long bytes = 0x1010101010101010;

  data_t *data = (data_t *)bytes;
}