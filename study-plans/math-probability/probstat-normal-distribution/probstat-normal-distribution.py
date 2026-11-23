from scipy.stats import norm

def normal_distribution(mu: float, sigma: float, x: float) -> dict:
    """
    Returns the z-score, CDF, PDF, and one-standard-deviation probability.
    """
    z_score=(x-mu)/sigma
    return {"cdf":norm.cdf(z_score),"pdf":norm.pdf(z_score)/sigma,"prob_within_1_std":float(norm.cdf(1) - norm.cdf(-1)),"z_score":z_score}
