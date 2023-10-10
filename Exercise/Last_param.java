class Solution {
  static String last_param(String[] param_1) {
    if (param_1.length > 0) {
      return param_1[param_1.length - 1];
    } else {
      return null;
    }
  }

  public static void main(String[] args) {
    String[] input = {"it", "is", "the", "truth"};
    System.out.println(last_param(input));
  }
}

