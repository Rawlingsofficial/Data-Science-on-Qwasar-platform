char* alpha_mirror(char* param_1)
{
    if (param_1 == 0) return 0;
  int i = 0;
  char c = param_1[0];

  while (c != '\0') {
    if (c >= 'a' && c <= 'z') 
      param_1[i] = 'm' - c + 'n';
    else if (c >= 'A' && c <= 'Z')
      param_1[i] = 'M' - c + 'N';
    c = param_1[++i];
  }
  return param_1;
}