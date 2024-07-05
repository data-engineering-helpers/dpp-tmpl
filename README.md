Cookiecutter template for the deployment of data processing pipelines (dpp)
===========================================================================

# Table of Content (ToC)



# Overview
This
[Cookiecutter template repository](https://github.com/data-engineering-helpers/dpp-tmpl)
quickstarts the deployment of data processing pipelines (dpp), sometimes also
referred as data transformation jobs, on cloud-based infrastructure.
Typically, data processing pipelines may be powered by
[Kubernetes](https://kubernetes.io/)
(_e.g._, with specific services like [AWS EKS](https://aws.amazon.com/eks/))
or by specific engines like
[Apache Spark compute engine](https://spark.apache.org/docs/latest/index.html).
Such specific engines are in turn operated either on specific services offered
by general purpose cloud providers (_e.g._,
[AWS EMR](https://aws.amazon.com/emr/) for Spark and Flink) or all-in-one
platforms (_e.g._, [DataBricks](https://databricks.com)).

Data processing jobs:
1. Take the shape of so-called data processing modules, which:
  * Capitalize the business knowledge through business-oriented software
    source code, in any of the supported programming languages (_i.e._,
	Scala, Python, SQL and potentially R)
  * Deliver software artifacts on artifact repositories (_e.g._,
	[AWS CodeArtifact](https://aws.amazon.com/codeartifact/))
  * Mainly rely on Apache Spark, but may also use alternatively simpler
    workloads (_e.g.,_, [DuckDB](https://duckdb.org/) or
	[Polars](https://pola.rs/)), which may be deployed on Kubernetes
2. Are deployed on compute engines (_e.g._, DataBricks for exploration and
   development purposes, AWS EMR for industrialization, Kubernetes for
   non-Spark or non-distributed work loads). The deployment relies on
   (Docker-like) containers, which:
   * Install the data processing software artifacts through the
     programming language native package systems (_e.g._, `pip` for Python
	 and `sbt` for Scala)
   * Are deployed on DataBricks, AWS EMR or AWS EKS

Even though the members of the GitHub organization may be employed
by some companies, they speak on their personal behalf and do not represent
these companies.
