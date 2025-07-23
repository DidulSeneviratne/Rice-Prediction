
# model_extent data needs to be like that

season_map = {'Maha': 0, 'Yala': 1}
district_list = df['District'].unique().tolist()

def predict_harvested(year, season, district, sown_hect, previous_yield):

    # Encode inputs
    season_encoded = season_map.get(season, 0)
    try:
        district_encoded = district_list.index(district.upper())
    except ValueError:
        raise ValueError(f"District '{district}' not found in the dataset.")

    # Create input DataFrame
    input_df = pd.DataFrame([{
        'Year': year,
        'Season_encoded': season_encoded,
        'District_encoded': district_encoded,
        'Sown(hect)': sown_hect,
        'Previous_Yield': previous_yield
    }])

    # Predict Harvested Extent
    predicted_extent = model_extent.predict(
        input_df[['Year', 'Season_encoded', 'District_encoded', 'Sown(hect)', 'Previous_Yield']]
    )[0]

    return round(predicted_extent, 2)

extent = predict_harvested(
    year=1999,
    season='Yala',
    district='POLONNARUWA',
    sown_hect=46144,
    previous_yield=4335
    # year=1982,
    # season='Yala',
    # district='BADULLA',
    # sown_hect=4369
)

print(f"Predicted Harvested Extent: {extent} hectares")


''' --------------------------------------------------------------------------------------------------------------------------------------------- '''

# model_production data needs to be like that

season_map = {'Maha': 0, 'Yala': 1}
district_list = df['District'].unique().tolist()

def predict_production(year, season, district, extent_hect, previous_yield):

    # Encode inputs
    season_encoded = season_map.get(season, 0)
    try:
        district_encoded = district_list.index(district.upper())
    except ValueError:
        raise ValueError(f"District '{district}' not found in the dataset.")

    # Create input DataFrame with correct feature names
    input_df = pd.DataFrame([{
        'Year': year,
        'Season_encoded': season_encoded,
        'District_encoded': district_encoded,
        'Extent Harvested(hect)': extent_hect,
        'Previous_Yield': previous_yield # Use the correct feature name
    }])

    # Predict Harvested Production
    predicted_production = model_prodiction.predict(
        input_df[['Year', 'Season_encoded', 'District_encoded', 'Extent Harvested(hect)', 'Previous_Yield']] # Use the correct feature names
    )[0]

    return round(predicted_production, 2)

production = predict_production(
    year=1999,
    season='Yala',
    district='POLONNARUWA',
    extent_hect=extent,
    previous_yield=4335
    # year=1982,
    # season='Yala',
    # district='BADULLA',
    # sown_hect=4369
)

print(f"Predicted Total Production: {production} hectares")