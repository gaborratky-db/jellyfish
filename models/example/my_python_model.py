def model(dbt, session):
  my_sql_model_df = dbt.ref("my_first_dbt_model")

  final_df = my_sql_model_df.where(my_sql_model_df.id.isNotNull())

  return final_df
