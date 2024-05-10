import { expect, test } from "vitest";
import { sort } from "../src/sort";

test("Test Sort Function", () => {
    expect(sort([7, 8, 12, 25, 28])).toEqual([7, 8, 12, 25, 28]);
    expect(sort([28, 14, 8, 4, 1])).toEqual([1, 4, 8, 14, 28]);
    expect(sort([1, 28, 2, 5, 14])).toEqual([1, 2, 5, 14, 28]);
    expect(sort([1, 1, 1, 1, 1])).toEqual([1, 1, 1, 1, 1]);
    expect(sort([])).toEqual([]);
    expect(["1", "2", "3", "4", "5"].sort()).toEqual(["1", "2", "3", "4", "5"]);
});