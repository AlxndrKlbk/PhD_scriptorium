def eos_rein():
  co2_export_frac=0.05
  if is_report_step ():
    if (fcmpr_2/fmpr)>co2_export_frac:
      co2_to_inject=fcmpr_2-(fmpr-fcmpr_2)*(co2_export_frac/(1-co2_export_frac))
      co2_sale_frac=1-co2_to_inject/fcmpr_2
    else:
      co2_sale_frac=1
    print(co2_sale_frac)
    add_keyword(
    """
    GRUPSALE
     FIELD 0 1  1 """+str(co2_sale_frac)+""" 1 1 1 1 1 1 1 1 /
    /
    """
    )