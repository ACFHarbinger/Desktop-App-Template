#include "desktop_app_template/greet.hpp"

#include <gtest/gtest.h>

TEST(Greet, ReturnsExpectedMessage) {
    EXPECT_EQ(desktop_app_template::greet("Desktop-App-Template"), "Hello, Desktop-App-Template!");
}

TEST(Greet, HandlesDefaultCase) {
    EXPECT_EQ(desktop_app_template::greet("world"), "Hello, world!");
}

