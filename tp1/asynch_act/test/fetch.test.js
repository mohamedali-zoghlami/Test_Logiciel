import { expect, test } from "vitest";
import { fetchRandomUser } from "../src/fetch";

test("Async Function", async () => {
    try {
      const data = await fetchRandomUser(); 
      console.log(data);
      expect(typeof data).toBe('object');
      expect(data).toHaveProperty('name');
      expect(data).toHaveProperty('email');
      expect(data).toHaveProperty('login');
    } catch (error) {
      fail('Should not throw any error');
    }
});