#include <benchmark/benchmark.h>

#include "desktop_app_template/greet.hpp"

static void BM_Greet(benchmark::State& state) {
    for (auto _ : state) {
        benchmark::DoNotOptimize(desktop_app_template::greet("world"));
    }
}
BENCHMARK(BM_Greet);

