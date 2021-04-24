#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-webfakes
Version  : 1.1.2
Release  : 6
URL      : https://cran.r-project.org/src/contrib/webfakes_1.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/webfakes_1.1.2.tar.gz
Summary  : Fake Web Apps for HTTP Testing
Group    : Development/Tools
License  : MIT
Requires: R-webfakes-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
without using the internet. It includes a web app framework with path
  matching, parameters and templates. Can parse various 'HTTP' request
  bodies. Can send 'JSON' data or files from the disk. Includes a web app

%package lib
Summary: lib components for the R-webfakes package.
Group: Libraries

%description lib
lib components for the R-webfakes package.


%prep
%setup -q -c -n webfakes
cd %{_builddir}/webfakes

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617641169

%install
export SOURCE_DATE_EPOCH=1617641169
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library webfakes
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library webfakes
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library webfakes
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc webfakes || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/webfakes/DESCRIPTION
/usr/lib64/R/library/webfakes/INDEX
/usr/lib64/R/library/webfakes/LICENSE
/usr/lib64/R/library/webfakes/Meta/Rd.rds
/usr/lib64/R/library/webfakes/Meta/features.rds
/usr/lib64/R/library/webfakes/Meta/hsearch.rds
/usr/lib64/R/library/webfakes/Meta/links.rds
/usr/lib64/R/library/webfakes/Meta/nsInfo.rds
/usr/lib64/R/library/webfakes/Meta/package.rds
/usr/lib64/R/library/webfakes/NAMESPACE
/usr/lib64/R/library/webfakes/NEWS.md
/usr/lib64/R/library/webfakes/R/webfakes
/usr/lib64/R/library/webfakes/R/webfakes.rdb
/usr/lib64/R/library/webfakes/R/webfakes.rdx
/usr/lib64/R/library/webfakes/credits/ciwetweb.md
/usr/lib64/R/library/webfakes/credits/redoc.md
/usr/lib64/R/library/webfakes/examples/hello/app.R
/usr/lib64/R/library/webfakes/examples/hello/views/test.txt
/usr/lib64/R/library/webfakes/examples/httpbin/app.R
/usr/lib64/R/library/webfakes/examples/httpbin/assets/httpbin.html
/usr/lib64/R/library/webfakes/examples/httpbin/data/deny.txt
/usr/lib64/R/library/webfakes/examples/httpbin/data/example.html
/usr/lib64/R/library/webfakes/examples/httpbin/data/example.json
/usr/lib64/R/library/webfakes/examples/httpbin/data/example.xml
/usr/lib64/R/library/webfakes/examples/httpbin/data/robots.txt
/usr/lib64/R/library/webfakes/examples/httpbin/data/utf8.html
/usr/lib64/R/library/webfakes/examples/httpbin/doc-template.hbs
/usr/lib64/R/library/webfakes/examples/httpbin/images/Rlogo.jpeg
/usr/lib64/R/library/webfakes/examples/httpbin/images/Rlogo.png
/usr/lib64/R/library/webfakes/examples/httpbin/images/Rlogo.svg
/usr/lib64/R/library/webfakes/examples/httpbin/images/Rlogo.webp
/usr/lib64/R/library/webfakes/examples/httpbin/openapi.yaml
/usr/lib64/R/library/webfakes/examples/send-file/Rlogo.png
/usr/lib64/R/library/webfakes/examples/send-file/app.R
/usr/lib64/R/library/webfakes/examples/static/app.R
/usr/lib64/R/library/webfakes/examples/static/public/bar/foo.txt
/usr/lib64/R/library/webfakes/examples/static/public/foo/bar.html
/usr/lib64/R/library/webfakes/examples/static/public/foo/bar.json
/usr/lib64/R/library/webfakes/help/AnIndex
/usr/lib64/R/library/webfakes/help/aliases.rds
/usr/lib64/R/library/webfakes/help/paths.rds
/usr/lib64/R/library/webfakes/help/webfakes.rdb
/usr/lib64/R/library/webfakes/help/webfakes.rdx
/usr/lib64/R/library/webfakes/html/00Index.html
/usr/lib64/R/library/webfakes/html/R.css
/usr/lib64/R/library/webfakes/tests/testthat.R
/usr/lib64/R/library/webfakes/tests/testthat/fixtures/output/webfakes_app.txt
/usr/lib64/R/library/webfakes/tests/testthat/fixtures/output/webfakes_app_process.txt
/usr/lib64/R/library/webfakes/tests/testthat/fixtures/output/webfakes_regexp.txt
/usr/lib64/R/library/webfakes/tests/testthat/fixtures/output/webfakes_request.txt
/usr/lib64/R/library/webfakes/tests/testthat/fixtures/output/webfakes_response.txt
/usr/lib64/R/library/webfakes/tests/testthat/fixtures/static/static.html
/usr/lib64/R/library/webfakes/tests/testthat/fixtures/static/subdir/static.json
/usr/lib64/R/library/webfakes/tests/testthat/fixtures/static2/static.html
/usr/lib64/R/library/webfakes/tests/testthat/fixtures/static2/static.tar.gz
/usr/lib64/R/library/webfakes/tests/testthat/fixtures/static2/subdir/static.json
/usr/lib64/R/library/webfakes/tests/testthat/fixtures/views/test-view.html
/usr/lib64/R/library/webfakes/tests/testthat/helper.R
/usr/lib64/R/library/webfakes/tests/testthat/setup.R
/usr/lib64/R/library/webfakes/tests/testthat/teardown.R
/usr/lib64/R/library/webfakes/tests/testthat/test-app-process.R
/usr/lib64/R/library/webfakes/tests/testthat/test-app.R
/usr/lib64/R/library/webfakes/tests/testthat/test-base64.R
/usr/lib64/R/library/webfakes/tests/testthat/test-delay.R
/usr/lib64/R/library/webfakes/tests/testthat/test-http-methods.R
/usr/lib64/R/library/webfakes/tests/testthat/test-httpbin.R
/usr/lib64/R/library/webfakes/tests/testthat/test-local.R
/usr/lib64/R/library/webfakes/tests/testthat/test-mime.R
/usr/lib64/R/library/webfakes/tests/testthat/test-mw-etag.R
/usr/lib64/R/library/webfakes/tests/testthat/test-mw-log.R
/usr/lib64/R/library/webfakes/tests/testthat/test-mw-multipart.R
/usr/lib64/R/library/webfakes/tests/testthat/test-mw-raw.R
/usr/lib64/R/library/webfakes/tests/testthat/test-mw-static.R
/usr/lib64/R/library/webfakes/tests/testthat/test-mw-urlencoded.R
/usr/lib64/R/library/webfakes/tests/testthat/test-oauth.R
/usr/lib64/R/library/webfakes/tests/testthat/test-path-matching.R
/usr/lib64/R/library/webfakes/tests/testthat/test-print.R
/usr/lib64/R/library/webfakes/tests/testthat/test-response.R
/usr/lib64/R/library/webfakes/tests/testthat/test-tmpl-glue.R
/usr/lib64/R/library/webfakes/tests/testthat/test-uuid.R
/usr/lib64/R/library/webfakes/views/authorize.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/webfakes/libs/webfakes.so
/usr/lib64/R/library/webfakes/libs/webfakes.so.avx2
