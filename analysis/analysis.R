# analysis.R — Evolution of Mosquito-Borne Diseases in Latin America 2015-2024: Database by Country and Disease
# DOI: 10.5281/zenodo.18880833
# Author: de la Serna Tuya, Juan Moisés · ORCID: 0000-0002-8401-8018
# License: CC0 1.0

# ── SETUP ──────────────────────────────────────────────────────────────────
# Install required packages if needed:
# install.packages(c("readr","ggplot2","dplyr","tidyr"))

library(readr)
library(ggplot2)
library(dplyr)

# ── LOAD DATA ──────────────────────────────────────────────────────────────
# Download dataset from: https://doi.org/10.5281/zenodo.18880833
# df <- read_csv("dataset.csv")

# Example with synthetic data
set.seed(42)
years <- 2000:2023
df <- data.frame(
  year = years,
    latin_americ = rnorm(length(years), 50, 15),
  dengue = rnorm(length(years), 50, 15),
  zika = rnorm(length(years), 50, 15),
  covid_19 = rnorm(length(years), 50, 15),
  stringsAsFactors = FALSE
)

cat("Dataset: Evolution of Mosquito-Borne Diseases in Latin Amer\n")
cat("DOI: 10.5281/zenodo.18880833\n")
cat("Dimensions:", nrow(df), "x", ncol(df), "\n\n")
print(head(df))
print(summary(df))

# ── VISUALIZATION ──────────────────────────────────────────────────────────
# Temporal trend
p1 <- df %>%
  tidyr::pivot_longer(-year, names_to="variable", values_to="value") %>%
  ggplot(aes(x=year, y=value, color=variable)) +
  geom_line(size=0.8) +
  geom_point(size=1.5) +
  labs(title="Evolution of Mosquito-Borne Diseases in Latin America 2",
       subtitle="DOI: 10.5281/zenodo.18880833",
       x="Year", y="Value",
       caption="de la Serna Tuya, Juan Moisés · 2026") +
  theme_minimal() +
  theme(legend.position="bottom")

ggsave("figures/analysis_output_r.png", p1, width=10, height=6, dpi=150)
cat("\nFigure saved: figures/analysis_output_r.png\n")

# ── CITATION ───────────────────────────────────────────────────────────────
cat("\nCitation:\n")
cat("de la Serna Tuya, Juan Moisés (2026). Evolution of Mosquito-Borne Diseases in Latin America 2015-2024: Datab. Zenodo. https://doi.org/10.5281/zenodo.18880833\n")
