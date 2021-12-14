package reverseBits;

import org.junit.Assert;
import org.junit.Test;

public class TestReverseBits {
	@Test
	public void test01() {
        ReverseBits solution = new ReverseBits();
		Assert.assertEquals(solution.reverseBits(1), 1);

	}

	@Test
	public void test02() {
        ReverseBits solution = new ReverseBits();
		Assert.assertEquals(solution.reverseBits(10),1000);
	}

	@Test
	public void test03() {
        ReverseBits solution = new ReverseBits();
        Assert.assertEquals(solution.reverseBits(9090), 4209);

	}
}