import { expect, test } from "vitest";
import { toUpperCase } from "../src/chaine";

test("Test UpperCase function", () => {
    expect(toUpperCase("hello")).toBe("HELLO");
    expect(toUpperCase("hello world")).toBe("HELLO WORLD");
    expect(toUpperCase("")).toBe("");
    expect(toUpperCase("123")).toBe("123");
    expect(toUpperCase("test))((")).toBe("TEST))((");
});