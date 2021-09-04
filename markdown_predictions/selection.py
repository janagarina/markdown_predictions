COLUMN_MAPPING = {
    "Libellé OP Com.":"delivery",
    "Vitrine collection":"window_display",
    "Cible":"target",
    "Sous-Cible":"sub_target",
    "Sexe":"gender",
    "Catégorie":"product_category",
    "Famille":"family",
    "Sous-Famille":"sub_family",
    "Macro catégorie": "macro_category",
    "Nom Ref":"reference_name",
    "RefCol":"reference",
    "Lib. RefCol":"description",
    "Coloris":"color",
    "Matière":"material",
    "Saisonnalité":"seasonality",
    "PVC France":"price",
    "Rang":"weekly_rank",
    "CA Net TTCSem.N":"turnover",
    "CA Net TTCSem.-1N":"turnover_w_sub1",
    "CA Net TTCSem.-2N":"turnover_w_sub2",
    "CA Net TTCSem.-3N":"turnover_w_sub3",
    "Qté venduesSem.N":"quantity_sold",
    "Qté venduesSem.-1N":"quantity_sold_sub1",
    "Qté venduesSem.-2N":"quantity_sold_sub2",
    "Qté venduesSem.-3N":"quantity_sold_sub3",
    "Taux de remiseSem.N":"discount_rate",
    "Taux de remiseSem.-1N":"discount_rate_sub1",
    "Stock PDVSem.N":"store_stock",
    "Stk transitN":"stock_transit",
    "Stock PDV + Transit":"total_store_stock",
    "CouvertureSem.N":"weekly_cover",
    "Tx EcoulSem.N":"sellthrough",
    "CA Net TTCCumulN":"cum_turnover",
    "Taux de remiseCumulN":"cum_discount_rate",
    "Qté venduesCumulN":"cum_quantity_sold",
    "Nb RCTen venteN":"num_sizes",
    "Nb PDVavec RC en venteN":"num_stores",
    "Semaine 1ère vteN":"first_week_sale",
    "DéfilementN":"rate_of_sale",
    "Tx EcoulCumulN":"cum_sellthrough",
    "Stk DispoEntrepotN":"warehouse_stock",
    "Stk DispoRALCdeGenN":"zero_stock",
    "Stk Dispopour RéassortN":"avail_warehouse_stock",
    "%":"markdown"
}

COLUMN_SELECTION = {"PRE": ["reference",
          "seasonality",
          "price",
          "weekly_rank",
          "turnover",
          "gender",
          "turnover_w_sub1",
          "turnover_w_sub2",
          "turnover_w_sub3",
          "quantity_sold",
          "product_category",
          "family",
          "macro_category",
          "reference_name",
          "sub_target",
          "quantity_sold_sub1",
          "quantity_sold_sub2",
          "quantity_sold_sub3",
          "discount_rate",
          "discount_rate_sub1",
          "store_stock",
          "stock_transit",
          "total_store_stock",
          "weekly_cover",
          "cum_turnover",
          "cum_discount_rate",
          "cum_quantity_sold",
          "num_sizes",
          "num_stores",
          "first_week_sale",
          "rate_of_sale",
          "cum_sellthrough",
          "warehouse_stock",
          "zero_stock",
          "avail_warehouse_stock",
          "markdown"],
 "POST": ["delivery",
         "window_display",
         "target",
         "sub_family",
         "reference",
         "description",
         "color",
         "material",
         "seasonality",
         "price",
         "weekly_rank",
         "turnover",
         "turnover_w_sub1",
         "turnover_w_sub2",
         "turnover_w_sub3",
         "quantity_sold",
         "quantity_sold_sub1",
         "quantity_sold_sub2",
         "quantity_sold_sub3",
         "discount_rate",
         "discount_rate_sub1",
         "store_stock",
         "stock_transit",
         "total_store_stock",
         "weekly_cover",
         "cum_turnover",
         "cum_discount_rate",
         "cum_quantity_sold",
         "num_sizes",
         "num_stores",
         "first_week_sale",
         "rate_of_sale",
         "cum_sellthrough",
         "warehouse_stock",
         "zero_stock",
         "avail_warehouse_stock",
         "markdown"],
    "reference_keys": ["reference", "season"]
}

