#include <iostream>
#include <string>
#include "spdlog/spdlog.h"
#include "lz4hc.h"

auto main() -> int {
    spdlog::warn("Hello, World!");
    std::string input = "Hello, World!";
    char buffer[1024];

    auto size = LZ4_compress_HC(input.c_str(), buffer, input.size(), 1024,
                                LZ4HC_CLEVEL_MAX);
    spdlog::info("Compressed size: {}", size);
    return 0;
}