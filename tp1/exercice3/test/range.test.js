import { expect, test } from "vitest";
import { isPriceInRange } from "../src//range";

test("Test range function", () => {
    expect(isPriceInRange(3, 0, 5)).toBeTruthy();
    expect(isPriceInRange(0, 0, 5)).toBeTruthy();
    expect(isPriceInRange(5, 0, 5)).toBeTruthy();
    expect(isPriceInRange(6, 0, 5)).toBeFalsy();
    expect(isPriceInRange(-1, 0, 5)).toBeFalsy();
});