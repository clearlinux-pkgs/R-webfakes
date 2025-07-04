#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v27
# autospec commit: 65cf152
#
Name     : R-webfakes
Version  : 1.4.0
Release  : 38
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/webfakes_1.4.0.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/webfakes_1.4.0.tar.gz
Summary  : Fake Web Apps for HTTP Testing
Group    : Development/Tools
License  : MIT
Requires: R-webfakes-lib = %{version}-%{release}
BuildRequires : R-curl
BuildRequires : buildreq-R

%description
without using the internet. It includes a web app framework with path
    matching, parameters and templates. Can parse various 'HTTP' request
    bodies. Can send 'JSON' data or files from the disk. Includes a web
    app that implements the 'httpbin.org' web service.

%package lib
Summary: lib components for the R-webfakes package.
Group: Libraries

%description lib
lib components for the R-webfakes package.


%prep
%setup -q -n webfakes
pushd ..
cp -a webfakes buildavx2
popd
pushd ..
cp -a webfakes buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1750869985

%install
export SOURCE_DATE_EPOCH=1750869985
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/webfakes/cert/localhost/ca.crt
/usr/lib64/R/library/webfakes/cert/localhost/ca.key
/usr/lib64/R/library/webfakes/cert/localhost/generate.sh
/usr/lib64/R/library/webfakes/cert/localhost/server.crt
/usr/lib64/R/library/webfakes/cert/localhost/server.csr
/usr/lib64/R/library/webfakes/cert/localhost/server.key
/usr/lib64/R/library/webfakes/cert/localhost/server.pem
/usr/lib64/R/library/webfakes/credits/ciwetweb.md
/usr/lib64/R/library/webfakes/credits/redoc.md
/usr/lib64/R/library/webfakes/examples/hello/app.R
/usr/lib64/R/library/webfakes/examples/hello/views/test.txt
/usr/lib64/R/library/webfakes/examples/httpbin/app.R
/usr/lib64/R/library/webfakes/examples/httpbin/assets/forms-post.html
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
/usr/lib64/R/library/webfakes/tests/testthat/_snaps/app-process.md
/usr/lib64/R/library/webfakes/tests/testthat/_snaps/app.md
/usr/lib64/R/library/webfakes/tests/testthat/_snaps/git-app.md
/usr/lib64/R/library/webfakes/tests/testthat/_snaps/mw-range-parser.md
/usr/lib64/R/library/webfakes/tests/testthat/_snaps/new-r/httpbin.md
/usr/lib64/R/library/webfakes/tests/testthat/_snaps/old-r/httpbin.md
/usr/lib64/R/library/webfakes/tests/testthat/_snaps/print.md
/usr/lib64/R/library/webfakes/tests/testthat/_snaps/request.md
/usr/lib64/R/library/webfakes/tests/testthat/fixtures/git-repo.tar.gz
/usr/lib64/R/library/webfakes/tests/testthat/fixtures/output/webfakes_app.txt
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
/usr/lib64/R/library/webfakes/tests/testthat/test-decode-url.R
/usr/lib64/R/library/webfakes/tests/testthat/test-delay.R
/usr/lib64/R/library/webfakes/tests/testthat/test-git-app.R
/usr/lib64/R/library/webfakes/tests/testthat/test-http-methods.R
/usr/lib64/R/library/webfakes/tests/testthat/test-httpbin.R
/usr/lib64/R/library/webfakes/tests/testthat/test-https.R
/usr/lib64/R/library/webfakes/tests/testthat/test-local.R
/usr/lib64/R/library/webfakes/tests/testthat/test-mime.R
/usr/lib64/R/library/webfakes/tests/testthat/test-mw-etag.R
/usr/lib64/R/library/webfakes/tests/testthat/test-mw-log.R
/usr/lib64/R/library/webfakes/tests/testthat/test-mw-multipart.R
/usr/lib64/R/library/webfakes/tests/testthat/test-mw-range-parser.R
/usr/lib64/R/library/webfakes/tests/testthat/test-mw-raw.R
/usr/lib64/R/library/webfakes/tests/testthat/test-mw-static.R
/usr/lib64/R/library/webfakes/tests/testthat/test-mw-urlencoded.R
/usr/lib64/R/library/webfakes/tests/testthat/test-oauth.R
/usr/lib64/R/library/webfakes/tests/testthat/test-path-matching.R
/usr/lib64/R/library/webfakes/tests/testthat/test-print.R
/usr/lib64/R/library/webfakes/tests/testthat/test-request.R
/usr/lib64/R/library/webfakes/tests/testthat/test-response.R
/usr/lib64/R/library/webfakes/tests/testthat/test-threads.R
/usr/lib64/R/library/webfakes/tests/testthat/test-tmpl-glue.R
/usr/lib64/R/library/webfakes/tests/testthat/test-uuid.R
/usr/lib64/R/library/webfakes/views/authorize.html

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/webfakes/libs/webfakes.so
/V4/usr/lib64/R/library/webfakes/libs/webfakes.so
/usr/lib64/R/library/webfakes/libs/webfakes.so
